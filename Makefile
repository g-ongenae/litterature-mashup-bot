.PHONY: cover tests
.DEFAULT: help

ENV_RUN = pipenv run

SOURCES =
TEST_DIR = ./tests

help:
	@echo "Read the ./README.md"

install-env:
	brew install pipenv || pip install --user pipenv

install:
	pipenv install

install-dev: install
	pipenv install --dev
	$(ENV_RUN) pre-commit install

commit:
	$(ENV_RUN) commitizen

lint:
	$(ENV_RUN) pylint ./{src,tests}/{**/,}*.py ./*.py

format:
	$(ENV_RUN) black --target-version py38 ./{**/**/,**/,}*.py

tests:
	$(ENV_RUN) pytest $(TESTS)

cover:
	$(ENV_RUN) pytest --cov=$(SOURCES) $(TESTS)

run:
	PORT=8080 $(ENV_RUN) python run.py
