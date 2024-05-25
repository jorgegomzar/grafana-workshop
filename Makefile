#!/usr/bin/make

generate_csv: poetry
	python scripts/get_data_from_ine.py
	
venv:
	python3 -m venv venv
	. venv/bin/activate

poetry: venv
	pip install poetry
	poetry install

up:
	docker compose up -d --force-recreate

down:
	docker compose down
