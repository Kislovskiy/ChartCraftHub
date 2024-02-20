.PHONY: install
install:
	python3 -m pip install --upgrade pip
	python3 -m pip install ".[dev]"
	python3 -m pip install --editable .

.PHONY: upgrade
upgrade:
	python3 -m pip install --upgrade .
	python3 -m pip install --upgrade ".[dev]"
	python3 -m pip install --upgrade ".[docs]"

.PHONY: test
test:
	python3 -m pytest tests

.PHONY: lint
lint:
	ruff check --fix-only .

.PHONY: format
format:
	ruff format .
