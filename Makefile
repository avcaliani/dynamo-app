.DEFAULT_GOAL := up

up:
	docker-compose up -d

down:
	docker-compose down

rebuild: down
	docker-compose build && docker-compose up -d

init-db:
	docker-compose exec cluster python scripts/dynamo.py init

start-api:
	docker-compose exec cluster uvicorn main:app --host "0.0.0.0" --port "9000"

.PHONY: up down rebuild init-db start-api
