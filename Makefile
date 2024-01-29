.PHONY: install
install:
	python3 -m pip install --upgrade pip
	python3 -m pip install ".[dev]"
	python3 -m pip install --editable .

.PHONY: test
test:
	python3 -m pytest tests

.PHONY: lint
lint:
	ruff check --fix-only .

.PHONY: format
format:
	ruff format .
