init_db:
	docker-compose exec db createdb -U postgres geodb
	docker-compose exec db psql -U postgres -c 'CREATE EXTENSION postgis;' geodb
