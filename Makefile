mongo-username = 'SATURAS'
mongo-password = 'TETRIANDOCH'

format:
	docker-compose exec backend bash -c "isort . && black ."

build-dev:
	cp -n ./config/.env.template ./config/.env
	docker-compose build

up-dev:
	docker-compose up

backend-bash:
	docker-compose exec backend bash

frontend-bash:
	docker-compose exec frontend bash

mongo-shell:
	docker-compose exec mongo bash -c "mongosh --username $(mongo-username) --password $(mongo-password)"
