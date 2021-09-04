postgres-user = postgres

format:
	docker-compose exec backend bash -c "isort . && black ."

build-dev:
	-cp -n ./config/.env.template ./config/.env
	docker-compose build

up-dev:
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
	docker-compose exec backend bash -c "alembic revision -m '$(message)'"