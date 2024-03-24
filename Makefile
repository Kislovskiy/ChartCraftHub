.PHONY: install
install:
	python3 -m pip install --upgrade pip
	python3 -m pip install ".[dev]"
	python3 -m pip install --editable .

.PHONY: install_devcontainer
install_devcontainer:
	sudo wget --content-disposition -P /usr/share/fonts/truetype/robotomono https://github.com/Kislovskiy/ChartCraftHub/blob/trunk/src/chartcrafthub/fonts/RobotoMono-Regular.ttf?raw=true
	sudo apt-get update && \
	sudo apt install fontconfig && \
	fc-cache -fv
	python3 -m pip install --upgrade pip
	python3 -m pip install ".[dev]"
	python3 -m pip install --editable .

.PHONY: install_docs
install_docs:
	python3 -m pip install ".[docs]"

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

.PHONY: docs
docs:
	cd docs; make html