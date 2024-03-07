# Pull base image
FROM python:3.10-slim as build

WORKDIR /code

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apt-get update && apt-get upgrade -y -q
# RUN apt-get install -y -q git

# Configuring poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

#Copying to code
COPY poetry.lock .
COPY pyproject.toml .
COPY system system

RUN poetry install --only main

ENTRYPOINT [ "sh", "-c" ]

FROM build as build-test

COPY tests tests
RUN poetry install --only dev

FROM build as local

CMD ["python -m system"]

FROM build-test as test

RUN poetry install --only dev

CMD ["coverage run -m unittest discover -v -s ./tests -p '*test*.py';coverage report;exit 0"]
