build:
	python3 -m pip install poetry
	python3 -m poetry install

test:
	python3 -m poetry run flake8 src
	PYTHONPATH=src python3 -m poetry run coverage run
	python3 -m poetry run coverage report
	python3 -m poetry run bandit -r src
	python3 -m poetry run safety check
	PYTHONPATH=src python3 -m poetry run mypy src
	
format:
	python3 -m poetry run black src
	python3 -m poetry run isort src

deploy-dev:
	sls deploy --stage dev





	
