test:
	python -m pytest -s

run:
	flask run

db-upgrade:
	flask db upgrade

db-makemigrations:
	flask db migrate
