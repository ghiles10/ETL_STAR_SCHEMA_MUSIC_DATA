import sys
sys.path.append(".")
sys.path.append("./src")

import pytest
from src.utils.utils import connection_object

# Définir un fixture pour créer une connexion à la base de données
# qui sera partagé par tous les tests de ce module
@pytest.fixture(scope="module")
def con_db():
    conn = connection_object()
    yield conn
    conn.close()

def test_create_database(con_db):
    """Vérifier si la base de données existe"""
    cur = con_db.cursor()
    cur.execute("SELECT datname FROM pg_database")
    result = cur.fetchall()
    assert "database" in [r[0] for r in result]

# Utiliser la marqueur paramétrique pour tester plusieurs tables
@pytest.mark.parametrize('table_name', ['songs', 'artists', 'users', 'time', 'songplays'])
def test_create_table(con_db, table_name):
    """ Vérifier si la table existe """
    
    cur = con_db.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    result = cur.fetchall()
    assert table_name in [r[0] for r in result]

# Utiliser la marqueur paramétrique pour tester plusieurs tables
@pytest.mark.parametrize('table_name', ['songs', 'artists', 'users', 'time', 'songplays'])
def test_insert_table(con_db, table_name):
    
    """  Vérifier si la table contient des données """
    
    cur = con_db.cursor()
    cur.execute(f"SELECT * FROM {table_name} limit 10")
    result = cur.fetchall()
    assert len(result) > 0
