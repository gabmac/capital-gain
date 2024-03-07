[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![poetry](https://img.shields.io/badge/maintained%20with-poetry-rgb(30%2041%2059).svg)](https://python-poetry.org/)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

# Technical Challenge: Capital Gain

The goal of this challenge is to  to implement a command line program (CLI) that calculates the tax to be paid on profits or losses from operations in the stock market.

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
|operation_type: OperationType|
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

### Pre-Commit and Code Smells

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


During development, you can change Docker Compose settings that will only affect
the local development environment in the file `docker-compose.yml`.

The changes on that file only affect the local development environment, not
the production environment. So, you can add "temporary" changes that help the
development workflow.

For example, the directory with the backend code is mounted as a Docker
"host volume", mapping the code you change live to the directory inside the container.
That allows you to test your changes right away, without having to build the
Docker image again. It should only be done during development.

For production, you should build the Docker image with a recent version of the
backend code, but during development, it allows you to make changes very fast.

To initialize the application, first you need it to build:

```bash
$ docker compose -f docker-compose.dev.yml build
```

Then run:

```bash
$ docker compose -f docker-compose.dev.yml up
```

Be sure that OpenSearch Node is up, what else the api can returns 500.

---

### Unit Tests and TDD

The project was developed using the Test-Driven Development strategy, which is based on a short cycle of repetitions that consists of Writing the test, Writing the code, and Refactoring the code.

The tests were created based on the acceptance criteria defined above, which were assembled according to the documentation of the challenge.

The tests run on a class-based architecture based on unittest.IsolatedAsyncioTestCase.

To test the backend, run:

```bash
$ poetry run unittest -v
```

To modify and add tests, go to `./<repository>/tests`.

The test will run automatically in the CI.

**Note**: To execute some tests, the database container needs to be up. To do this,
you can run:

```bash
$ docker compose -f docker-compose.dev.yml up dynamodb-local
```

#### Test Coverage

Because the test scripts forward arguments to `unittest`, to run the tests in a
running stack with coverage with terminal reports:

```bash
$ poetry run coverage run -m unittest -v
$ poetry run coverage report
```

To generate HTML report runs:

```bash
$ poetry run coverage html
```

You can use `docker compose` to run tests too:

```bash
$ docker compose -f docker-compose.test.yml build
$ docker compose -f docker-compose.test.yml up
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
