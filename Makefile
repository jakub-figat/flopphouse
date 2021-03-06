postgres-user = postgres
postgres-database = postgres
revision = head

format:
	docker-compose exec backend bash -c "isort . && black ."

build-dev:
	-cp -n ./config/.env.template ./config/.env
	docker-compose build

up-dev:
	make migrate
	docker-compose up

backend-bash:
	docker-compose exec backend bash

frontend-bash:
	docker-compose exec frontend bash

db-bash:
	docker-compose exec db bash

db-shell:
	docker-compose exec db psql -U $(postgres-user)

alembic-revision:
	docker-compose run --rm backend bash -c "alembic revision -m '$(message)'"

migrate:
	docker-compose run --rm backend bash -c "alembic upgrade $(revision)"

recreate-db:
	docker-compose exec db bash -c "runuser postgres -c 'dropdb $(postgres-database); createdb $(postgres-database)'"
	docker-compose exec db psql -U postgres -a -f /docker-entrypoint-initdb.d/init-postgres.sql
	make migrate

test:
	docker-compose exec backend bash  -c "coverage run --source=src -m pytest -s $(location)"

coverage-html:
	docker-compose exec backend bash -c "coverage html"

