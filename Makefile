.PHONY: install run test

install:
	poetry install

run:
	poetry run python main.py
