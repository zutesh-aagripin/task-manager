default: help

.PHONY: run
run: # run docker-compose.yml, which starts the pg database and runs the service in separate containers.
	docker-compose up

.PHONY: db-prepare
db-prepare: #create the migration for db. An initial migration is available that creates tables in default schema. Depends on the .env file for db connection.
	alembic revision --message="init"  --autogenerate

.PHONY: db-init
db-init: # create the necessary tables in database. Database must be up. Depends on the .env file for db connection
	alembic upgrade head

.PHONY: reqs
reqs: # install required modules for project
	pip install -r requirements.txt

.PHONY: run-app
run-app: # run only the service (if you have the database available)
	uvicorn main:app --host "0.0.0.0" --port "8000"

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

