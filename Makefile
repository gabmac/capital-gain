
build-unit-test:
	docker build -t capital-gain-test --target=test . --no-cache

build-application:
	docker build -t capital-gain-local --target=local . --no-cache

build-cases-test:
	docker build -t capital-gain-case --target=test-case .

build-all:
	build-test
	build-application

run-unit-test:
	docker run capital-gain-test

run-cases-test:
	docker run capital-gain-case

run:
	docker run -i capital-gain-local
