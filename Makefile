# Variables
VENV_NAME=env
APP=src/extract_transform/app.py
REQS=src/requirements.txt

$(VENV_NAME):
	python -m venv $(VENV_NAME)

install: $(VENV_NAME)
	. $(VENV_NAME)/bin/activate && pip install -r $(REQS)

run: install
	. $(VENV_NAME)/bin/activate && python $(APP)

test: run
	pip install pytest==7.0.1 
	pytest

clean:
	rm -rf $(VENV_NAME)

all: install run test clean 