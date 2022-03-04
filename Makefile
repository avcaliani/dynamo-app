.DEFAULT_GOAL := help

help:
	@echo ""
	@echo "🦖 AVAILABLE TASKS"
	@echo "  up            Start docker containers."
	@echo "  down          Teardown docker containers."
	@echo "  rebuild       Rebuild development image and restart the containers."
	@echo "  bash          Open development container bash."
	@echo "  init-db       Initialize DynamoDB."
	@echo "  start-api     Start FastAPI service locally."
	@echo ""

up:
	docker-compose up -d

down:
	docker-compose down

rebuild: down
	docker-compose build && docker-compose up -d

bash:
	docker-compose exec cluster bash

init-db:
	docker-compose exec cluster python scripts/dynamo.py init

start-api:
	docker-compose exec cluster uvicorn main:app --host "0.0.0.0" --port "9000" --reload

.PHONY: help up down rebuild bash init-db start-api
