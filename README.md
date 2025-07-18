# AWS Serverless FastAPI Template

A production-ready template for deploying a FastAPI application as an AWS Lambda function using Docker, Serverless Framework, and Mangum. Includes local development with Docker Compose, robust logging, and a sample search endpoint.

---

## Features

- **FastAPI**: Modern, fast (high-performance) web framework for building APIs.
- **AWS Lambda**: Serverless deployment using [Mangum](https://github.com/jordaneremieff/mangum) as the ASGI adapter.
- **Docker**: Containerized development and deployment environments.
- **Serverless Framework**: Infrastructure as code for AWS Lambda deployments.
- **Testing**: Pytest-based test suite with request mocking.
- **Logging**: Structured JSON logging via `python-json-logger`.
- **CI/CD**: GitHub Actions workflow for automated testing.
- **Type Checking & Linting**: Mypy, Flake8, Black, Isort, Bandit, and Safety.

---

## Project Structure
```

├── compose/ # Dockerfiles for dev and lambda
├── docs/ # Documentation
├── src/ # Application source code
│ ├── main.py # FastAPI app and Lambda handler
│ ├── logger.py # Logging setup
│ ├── settings.py # App and logger config
├── tests/ # Pytest test suite
├── serverless.yaml # Serverless Framework config
├── docker-compose.yml # Local dev environment
├── Makefile # Common commands
├── requirements.txt # Python dependencies (exported from Poetry)
├── pyproject.toml # Poetry project config
├── README.md # This file
```

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.8+
- [Poetry](https://python-poetry.org/)
- AWS CLI (for deployment)
- Serverless Framework (`npm install -g serverless`)

### Local Development

1. **Build and start the dev environment:**
    ```sh
    make build
    docker-compose up --build
    ```
    The API will be available at http://localhost:8000.

2. Stop the environment:
    ```
    docker-compose down
    ```

3. Running Tests
    ```
    make test
    ```
    This runs linting, type checks, security checks, and the test suite with coverage.

## Deployment
Deploy to AWS Lambda
1. Configure AWS credentials (see AWS docs)
2. Deploy using Serverless Framework:
    ```
    make deploy-dev
    ```
    This builds the Docker image and deploys the Lambda function.

## Configuration
* **App settings**: See settings.py
* **Logging**: Structured JSON logs, configurable via environment variables.
* **Serverless**: See serverless.yaml for AWS Lambda and API Gateway setup.

## Development Notes
* **Add dependencies**: Use Poetry to add packages, then export to requirements.txt.
    ```
    poetry add <package>
    poetry export -f requirements.txt --output requirements.txt
    ```
* **Formatting**: Run `make format` to auto-format code with black and isort.
* **CI/CD**: See default.yml for GitHub Actions setup.

