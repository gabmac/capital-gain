
build-unit-test:
	docker build -t capital-gain-test --target=test . $(CACHE)

build-application:
	docker build -t capital-gain-local --target=local . $(CACHE)

build-cases-test:
	docker build -t capital-gain-case --target=test-case . $(CACHE)

build-all-tests:
	docker build -t capital-gain-test --target=test . $(CACHE)
	docker build -t capital-gain-case --target=test-case . $(CACHE)

build-all:
	docker build -t capital-gain-test --target=test . $(CACHE)
	docker build -t capital-gain-case --target=test-case . $(CACHE)
	docker build -t capital-gain-local --target=local . $(CACHE)


run-all-tests:
	docker run capital-gain-test
	docker run capital-gain-case

build-run-all-tests: build-all-tests run-all-tests


run-unit-test:
	docker run capital-gain-test

run-cases-test:
	docker run capital-gain-case

run:
	docker run -i capital-gain-local
