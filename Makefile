install:
    pip install -r requirements.txt

createdb:
    psql -c 'create database database;' -U postgres
    
run:
    python3 extract_transform/app.py




