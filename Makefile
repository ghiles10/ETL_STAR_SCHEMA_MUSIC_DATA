install:
    pip install -r requirements.txt

run:
    python3 extract_transform/app.py

createdb:
    psql -c 'create database database;' -U postgres


