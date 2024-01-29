.DEFAULT_GOAL:=all

.PHONY: install
install:
	python3 -m pip install --upgrade pip
	python3 -m pip install ".[dev]"
	python3 -m pip install --editable .

.PHONY: lint
lint:
	ruff check --fix-only .

.PHONY: format
format:
	ruff format .
