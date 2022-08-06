# Score-Server

## Setup initialize

1. docker-compose run --entrypoint "poetry install" fastapi
2. docker-compose build --no-cache

## Migrations

1. docker-compose exec fastapi poetry run alembic revision --autogenerate -m"~~~~" (if sqlalchemy のモデルを作成したとき)
2. docker-compose exec fastapi poetry run alembic upgrade head
