# 🦖 Dynamo App

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

# 👇 Start your own docker environment.
make up init-db
```

Finally, execute the script.

```bash

# Start the API
make start-api
```

### ⚗️ Examples

#### API Home

```json5
// curl http://localhost:9000/ | json_pp -json_opt pretty,utf8
{
  "contact": {
    "email": "anthony@github.com",
    "name": "Anthony Caliani",
    "url": "https://github.com/avcaliani"
  },
  "description": "⚡️Fast API + 🦖 DynamoDB",
  "license": {
    "name": "MIT License",
    "url": "https://opensource.org/licenses/MIT"
  },
  "title": "🦖 Dynamo App - v1.0.0"
}
```

#### Creating new user

```bash
curl -X 'POST' \
  'http://localhost:9000/users' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{ 
          "document": "68979767000148", 
          "name": "anthony", 
          "birthdate": "1997-04-09", 
          "score": { "value": 7.5, "status": "😎" } 
      }' | json_pp -json_opt pretty,utf8
```

```json5
{
  "ResponseMetadata": {
    "HTTPHeaders": {
      "content-length": "2",
      "content-type": "application/x-amz-json-1.0",
      "date": "Fri, 04 Mar 2022 14:57:37 GMT",
      "server": "Jetty(9.4.18.v20190429)",
      "x-amz-crc32": "2745614147",
      "x-amzn-requestid": "0592f654-19a2-4a48-a943-3540b06d2d3c"
    },
    "HTTPStatusCode": 200,
    "RequestId": "0592f654-19a2-4a48-a943-3540b06d2d3c",
    "RetryAttempts": 0
  }
}
```

#### Retrieving a specific user

````json5
// curl http://localhost:9000/users/68979767000148 | json_pp -json_opt pretty,utf8
{
  "birthdate": "1997-04-09",
  "created_at": "2022-03-04 15:13:42",
  "document": "68979767000148",
  "enabled": true,
  "name": "anthony",
  "score": {
    "status": "😎",
    "value": 7.5
  },
  "updated_at": "2022-03-04 15:13:42"
}
````

#### Retrieving all users

````json5
// curl http://localhost:9000/users | json_pp -json_opt pretty,utf8
[
  {
    "birthdate": "1997-04-09",
    "created_at": "2022-03-04 15:13:42",
    "document": "68979767000148",
    "enabled": true,
    "name": "anthony",
    "score": {
      "status": "😎",
      "value": 7.5
    },
    "updated_at": "2022-03-04 15:13:42"
  }
]
````

## References

- [Medium: FastAPI + DynamoDB](https://medium.com/nerd-for-tech/introduction-to-fastapi-and-local-dynamodb-595c990ed0f8)