# Score-Server

## Setup initialize

1. docker-compose run --entrypoint "poetry install" fastapi
2. docker-compose build --no-cache

## Migrations

1. docker-compose exec fastapi poetry run alembic revision --autogenerate -m"~~~~" (if sqlalchemy のモデルを作成したとき)
2. docker-compose exec fastapi poetry run alembic upgrade head

## DATABASE initialize
### DELETE TABLE
1. docker-compose exec postgres bash
2. psql -d score-server -U fastapi
3. DELETE FROM users;
4. DELETE FROM scores;
### exec seed.py
1. docker-compose exec fastapi poetry run bash
2. python db/seed.py

