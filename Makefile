# Variables
VENV_NAME=env
APP=src/extract_transform/app.py
REQS=src/requirements.txt

# Créer l'environnement virtuel
$(VENV_NAME):
	python -m venv $(VENV_NAME)

# Installer les dépendances
install: $(VENV_NAME)
	. $(VENV_NAME)/bin/activate && pip install -r $(REQS)

# Lancer l'application
run: install
	. $(VENV_NAME)/bin/activate && python $(APP)

# Lancer les tests
test: run
	pip install pytest==7.0.1 
	pytest

# Nettoyer les fichiers temporaires
clean:
	rm -rf $(VENV_NAME)

# Tout exécuter
all: install run test