build:
	python3 -m pip install poetry
	python3 -m poetry install

test:
	python3 -m poetry run flake8 src	 			# Linting
	python3 -m poetry run pytest 		 			# Unit Test
	python3 -m poetry run bandit src 				# Security Checks
	PYTHONPATH=src python3 -m poetry run mypy src	# Static Checks
	
format:
	python3 -m poetry run black src	 				# PEP8 Autoformat
	python3 -m poetry run isort src					# Sort Modules

deploy-dev:
	sls deploy --stage dev





	
