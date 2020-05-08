PHONY: build

build-image: build
	docker build --no-cache -t vega-api:dev .

docker-stop:
	docker rm -f vega-api || true

docker-run: build-image docker-stop
	docker run --name vega-api -p 8000:8000 vega-api:dev

run-image: docker-run

build:
	pip install --upgrade pip; pipenv install; pipenv install --dev;\
	pipenv run python -m flake8 vega/
	pipenv run python manage.py test --settings=config.test

db-migrate:
	pip install --upgrade pip; pipenv install --dev;\
	pipenv run python manage.py migrate

test:
	pipenv run coverage run manage.py test --settings=config.test
	coverage report -m
