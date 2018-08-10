SHELL := bash
PATH := ./venv/bin:${PATH}
PYTHON=python3.7

default: install

venv:
	$(PYTHON) -m venv venv
	pip install --quiet --upgrade pip

clean:
	rm -rf venv/

install: venv
	pip install --quiet -r requirements.txt

lint:
	pycodestyle killer_queen tests

install-dev: install
	pip install --quiet -r requirements-dev.txt
