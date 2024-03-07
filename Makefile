
build-unit-test:
	docker build -t capital-gain-test --target=test . --no-cache

build-application:
	docker build -t capital-gain-local --target=local . --no-cache

build-all:
	build-test
	build-application

run-unit-test:
	docker run capital-gain-test

run:
	docker run capital-gain-local
