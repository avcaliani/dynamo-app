# Dynamo App

![#](https://img.shields.io/badge/python-3.10.x-yellow.svg)

## Quick Start

Create your Python virtual environment...

```bash
# 👇 Setting PyEnv version
pyenv local 3.10.0

# 👇 Virtual Environment
python -m venv .venv \
  && source .venv/bin/activate \
  && pip install --upgrade pip
 
# 👇 Install Dependencies
poetry install
```

Finally, execute the script.

```bash
# Start docker containers
make up

# Init DynamoDB
make init-db

# Start the API
make start-api
```

## References

- [Medium: FastAPI + DynamoDB](https://medium.com/nerd-for-tech/introduction-to-fastapi-and-local-dynamodb-595c990ed0f8)