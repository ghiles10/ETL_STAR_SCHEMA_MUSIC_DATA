import sys 
sys.path.append(".")
sys.path.append("./src")

import pytest 
from src.utils.utils import connection_object 

@pytest.fixture(scope="module")
def con_db() :  
    
    conn = connection_object()
    
    yield conn
    conn.close()
    
def test_create_database(con_db) : 
    
    cur = con_db.cursor()
    cur.execute("SELECT datname FROM pg_database")
    result = cur.fetchall()
    assert "database" in [r[0] for r in result] 

def test_create_table(con_db) : 
    
    cur = con_db.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    result = cur.fetchall()
    assert "songs" in [r[0] for r in result]