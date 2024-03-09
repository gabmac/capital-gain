# Build stage
FROM python:3.11-slim as build

WORKDIR /code

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Copy your application code and install dependencies
COPY poetry.lock pyproject.toml ./


# Install only main dependencies
RUN poetry install --only main
COPY system system

FROM build AS build-test

COPY tests tests
RUN poetry install --only dev

# Final stage
FROM gcr.io/distroless/python3-debian12:latest AS local

COPY --from=build /usr/local/lib/python3.11/site-packages /usr/lib/python3.11
COPY --from=build /code /code
WORKDIR /code

ENTRYPOINT ["/usr/bin/python", "-m", "system"]

FROM build-test AS test
ENTRYPOINT [ "sh", "-c" ]
CMD ["coverage run -m unittest discover -v -s ./tests -p '*test*.py';coverage report;exit 0"]

FROM build AS test-case

COPY cases cases

ENTRYPOINT [ "./cases/test_case.sh" ]
