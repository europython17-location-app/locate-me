start:
	docker-compose build
	docker-compose up -d
	docker-compose exec db createdb -U postgres geodb || true
	docker-compose exec db psql -U postgres -c 'CREATE EXTENSION postgis;' geodb || true
	python3 manage.py runserver 0.0.0.0:8000
