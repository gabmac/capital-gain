[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Coverage](/coverage.svg)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![poetry](https://img.shields.io/badge/maintained%20with-poetry-rgb(30%2041%2059).svg)](https://python-poetry.org/)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

# Technical Challenge: Capital Gain

The goal of this challenge is to  to implement a command line program (CLI) that calculates the tax to be paid on profits or losses from operations in the stock market.

## Run Application

To run the application you need to install [docker](#docker) and to make it easier you can install [make](#make).

Using docker:
```bash
$ docker build -t capital-gain-local --target=local . --no-cache
$ docker run -i capital-gain-local
```

Using make:
```bash
$ make build-application
$ make run
```

For both cases the build is only needed on the first time.

## **Acceptance Criteria**

### **Methodology**
For this challenge, we will be adopting the BDD (Behavior-Driven-Development) methodology. BDD is an extension of TDD (Test-Driven-Development) that emphasizes the behavior of the system.

### **User Stories**
User stories will be structured using the format:
- **"As a [Role], I want [Action], Because [Outcome/Benefit]"**.

This format helps in clearly defining the user's role, the action they want to perform, and the expected outcome or benefit of that action.

### **Acceptance Tests**
Acceptance tests will be written in the **Gherkin** language. The Gherkin language uses keywords like:
- **Scenario**: Defines a particular behavior of the system.
- **Given**: Describes the initial context or state.
- **When**: Describes the action that triggers the behavior.
- **And**: Provides additional conditions or actions.
- **Then**: Describes the expected outcome or result.

Using Gherkin for acceptance tests ensures that the tests are easily readable and can be understood by both technical and non-technical stakeholders.

---

## **User Story**

1.  **User Story: Calculating Taxes on Stock Market Transactions**
     - **As** a stock market investor,
     - **I want** a tool that calculates the taxes to be paid on my profits or losses from stock market transactions,
     - **Because** I need to accurately assess the financial outcomes of my trading activities, considering the type of operation, cost per unit, and the quantity of shares traded, to determine the tax obligation.

---

## **BDD Scenario**

**Feature**: Simple Tax Calculation on Stock Sales
**Background**:Given a stock trader needs to know the tax implications of their sell transactions

1. **Scenario**: Tax on Profitable Sales

    - **Given** the trader sells stocks at a profit
    - **When** the sale's total (unit cost * quantity) value exceeds R$ 20,000.00
    - **And** the selling price is higher than the *weighted average price*
    - **Then** a 20% tax is calculated on the profit

2. **Scenario**: Loss Adjustment

    - **Given** the trader has previously sold stocks at a loss
    - **When** they sell other stocks at a profit
    - **Then** the previous loss is subtracted from the current profit before tax calculation

3. **Scenario**: No Tax Under Threshold

    - **Given** the sale's total value is R$ 20,000.00 or less
    - **When** the trader sells stocks
    - **Then** no tax is applied regardless of profit or loss

4. **Scenario**: No Tax on Purchases

    - **Given** the trader buys stocks
    - **When** transactions are analyzed for tax
    - **Then** purchases are excluded from tax calculation

---

## **DDD**

In the challenge, we have a very well-defined objective, so we were able to identify only one domain. With the rules and acceptance criteria already defined above, our next step will be to define the entities and value objects."

### **Entities**
- Entities represents a domain objects that are defined by their identity, rather than by their attributes with distinct life cicle

|Operation|
|---|
|type: OperationType|
|unit-cost:float|
|quantity: int|
|tax:float|

---

## Package Manager

By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.

To install poetry you need to run:
```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```
**Note**: Pay Attention here! You may need to change the poetry path on `.bashrc`

From `./<repository>` you can install all the dependencies with:

```bash
$ poetry install
```

Then you can start a shell session with the new environment with:

```bash
$ poetry shell
```

From `./<repository>` you can update all the dependencies with:

```bash
$ poetry update
```

If you want to upgrade poetry you will need to run:
```console
$ poetry self update
```
---

### Useful Packages

* [**Pydantic**](https://docs.pydantic.dev/latest/) - Pydantic is the most widely used data validation library for Python. Here it is used for operations data manipulation.

---

## Pre-Commit and Code Smells

Before **any** commit we run a set of hooks that help us with the quality of the code.

The main code smells are:

1. **Black** - Python Code Formatter
2. **AutoFlake** - Removes Unused Imports
3. **Isort** - Sort Imports
4. **Flake8** - Linting and Checking for Python Errors
5. **Pylint** - Code Analysis for Python
6. **MyPy** - Static Typing for Python
7. **[Conventional Commit](https://www.conventionalcommits.org/en/v1.0.0/)** - Force to use correct message for commit
8. **Bandit** -  Designed to find common security issues in Python code
9. **Pip Audit** - Tool for scanning Python environments for packages with known vulnerabilities

To install you need to run:

```Bash
$ poetry run pre-commit install
```

After that, every commit you execute will run all the hooks.

---


## Make

The make command compiles different program pieces and builds a final executable. The purpose of make is to automate file compilation, making the process simpler and less time-consuming. The command works with any programming language as long as the compiler can be executed with a shell command. Everything is orchestrated based on Makefile

- **Ubuntu:** [Install Make on Ubuntu](https://ioflood.com/blog/install-make-command-linux/#:~:text=In%20most%20Linux%20distributions%2C%20the,command%20sudo%20yum%20install%20make%20.)
- **Mac:** [Install Make on Mac](https://formulae.brew.sh/formula/make)
- **Windows:** [Install Make on Windows](https://gnuwin32.sourceforge.net/packages/make.htm)


## Docker

Docker is an open-source platform that automates the deployment, scaling, and management of applications. It does this through containerization, a lightweight form of virtualization.

Containers can be thought of as isolated environments where applications can run. They include everything that an application needs to run, including the code, runtime, system tools, libraries, and settings. This means that the application will run the same way regardless of the environment it's in.

The key advantages of Docker include:

  1. Consistency: Since a Docker container bundles its own software, libraries, and dependencies, it ensures consistency across multiple development, testing, and production environments.

  2. Isolation: Containers are isolated from each other and from the host system, improving security and allowing multiple containers to run on the same system without interfering with each other.

  3. Portability: Containers can be run on any system that supports Docker, making it easy to deploy applications across multiple environments or cloud platforms.

  4. Scalability: Multiple containers can be run on a single host, and containers can be easily added or removed as needed, making Docker highly scalable.

To run the project with Docker, it is necessary to have it installed on your machine. If you don't have it, follow the instructions from the links:
- **Ubuntu:** [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- **Mac:** [Install Docker Engine on Mac](https://docs.docker.com/desktop/install/mac-install/)
- **Windows:** [Install Docker Engine on Windows](https://docs.docker.com/desktop/install/windows-install/)

### [Distroless Images](https://github.com/GoogleContainerTools/distroless?tab=readme-ov-file)

Distroless" images contain only your application and its runtime dependencies. They do not contain package managers, shells or any other programs you would expect to find in a standard Linux distribution. It is based on a extremely slimmed Linux distribution which contains runtime and application only, nothing else.

1. **Reduced Attack Surface**: By excluding unnecessary tools, binaries, and shell, Distroless images offer a smaller surface for potential attacks. There’s simply less in the image that can be exploited.
2. **Minimized Vulnerabilities**: With fewer components in the image, there are fewer potential points of failure. This can reduce the number of vulnerabilities and the frequency of required patches.
3. **No Shell**: Distroless images don’t contain a shell. This means if an attacker manages to get into the container, they won’t have a shell to execute further malicious commands, making it more challenging to move laterally or escalate privileges.
4. **Clearer Dependency Management**: By including only what’s necessary to run the application, it’s clearer what dependencies are present, making it easier to manage and update them. This clarity ensures that security patches are more straightforward to track and apply.

*In this application only the system container will run with this, the containers that mean to be used with test, keep it using `python-slim`

---

## Unit Tests and TDD

The project was developed using the Test-Driven Development strategy, which is based on a short cycle of repetitions that consists of Writing the test, Writing the code, and Refactoring the code.

The tests were created based on the acceptance criteria defined above, which were assembled according to the documentation of the challenge.

The tests run on a class-based architecture based on unittest.IsolatedAsyncioTestCase.

To test the backend, run:

```bash
$ poetry run unittest discover -v -s ./tests -p '*test*.py
```

To modify and add tests, go to `./<repository>/tests`.

The test will run automatically in the CI.

### Test Coverage

Because the test scripts forward arguments to `unittest`, to run the tests in a
running stack with coverage with terminal reports:

```bash
$ poetry run unittest discover -v -s ./tests -p '*test*.py
$ poetry run coverage report
```

To generate HTML report runs:

```bash
$ poetry run coverage html
```

You can use `docker` to run tests too:

```bash
$ docker build -t capital-gain-case --target=test-case .
$ docker run capital-gain-test
```

You can use `make` to run tests:
```bash
$ make build-unit-test
$ make run-unit-test
```

---

## Cases

If you want to run and compare with the cases that came in project you can run:

```bash
$ docker build -t capital-gain-case --target=test-case .
$ docker run capital-gain-case
```


```bash
$ make build-cases-test
$ make run-cases-test
```

---

## Clean Architecture

![image](https://miro.medium.com/v2/resize:fit:720/format:webp/1*0u-ekVHFu7Om7Z-VTwFHvg.png)


Clean architecture is a software architecture pattern proposed by Robert C. Martin, also known as Uncle Bob. It aims to separate concerns within a system, promoting a modular, testable, and easy-to-maintain design.

The main idea behind clean architecture is to establish a clear and defined separation between the different layers of the system, with each layer having specific and well-defined responsibilities. This separation allows the inner layers to be independent of the outer layers, resulting in loose coupling and greater flexibility.

Clean architecture follows the Dependency Inversion Principle (DIP) and the Single Responsibility Principle (SRP), written on [SOLID](https://medium.com/desenvolvendo-com-paixao/o-que-%C3%A9-solid-o-guia-completo-para-voc%C3%AA-entender-os-5-princ%C3%ADpios-da-poo-2b937b3fc530). The Dependency Inversion Principle states that high-level modules should not depend on low-level modules, but on abstractions. The Single Responsibility Principle, on the other hand, asserts that each class or component should have only one reason to change.

### Structure

Clean architecture is composed of several layers, which typically include:

**Domain**: The domain layer is the core of the system and contains the business rules and main entities.

**Application**: The application layer is responsible for orchestrating the actions of the system, applying the business rules of the entity layer.

**Infrastructure**: This is the layer responsible for implementing technical details, such as access to databases, calls to external services, etc.

### Directory Structure

#### .github
Github Config files

*PULL_REQUEST_TEMPLATE.md* -> A Template for pull requests, this way all PR`s can be standardized

*workflows/* -> In this directory there is some workflow that help with the pipeline
* *linter.yml* -> Run all the hooks explained in [pre-commit](#pre-commit-and-code-smells)
* *merge_main.yml* -> Every Pull Request has merge from main the base branch to keep it updated
* *pull_request_labeler* -> Helps to give at least on label per pull request
* *release.yml* -> Runs Everytime that a Pull Request is merged, it creates a relase with tag, helping to version the project and keep a changelog of all the system.
* *test_case.yml* -> runs the project cases and compare with the solution
* *update_package.yml* -> Update the third party packages
* *tests.yml* -> Run the unit tests
* *validation.yml* -> Orchestrate all the pipeline in every Pull Request

#### system
Here there is all the application files

#### tests
Suite tests

#### cases
There are all example project cases

* *<<caseno>>_input* -> input for case
* *<<caseno>>_output* -> expected system output
* *test_case.sh* -> Run the application for each input and compares with expected output


#### Pipeline

Every Pull Request follows:

![Pull Request](/images/pull_request.PNG)

After the merge on main, there will be a release:

![Release](/images/release.PNG)
