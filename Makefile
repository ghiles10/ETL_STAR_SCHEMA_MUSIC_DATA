# Variables
APP=src/extract_transform/app.py
REQS=requirements.txt

install: 
	pip install -r $(REQS)

run: install
	python $(APP)

lint: install
	pip install pylint
	pylint --disable=R,C src/

test: run
	pip install pytest==7.0.1 
	pytest

all: install run lint test