from pyspark.sql import SparkSession
import psycopg2
from utils.config import DB_DETAILS

def insert(table, cur, query):
    
    """this function insert data into the table"""
    
    for row in range(table.count()):
        cur.execute(query, tuple(table.collect()[row]) )
        
def spark_session(): 

    """Create a spark session to run the ETL pipeline. 
    Returns: 
        spark_session: Spark session object. 
    """ 
    
    session = SparkSession.builder.appName('ETL').getOrCreate() 

    return session
    
def postgres_connection(db_host, db_name, db_user, db_pass):

    connection = psycopg2.connect(f"dbname={db_name} user={db_user} host={db_host} password={db_pass}")

    return connection 

def connection_object(): 

    """ creates the object connection that connects us to the database """
    
    conn = postgres_connection(db_host = DB_DETAILS['db_host'],
                                db_name = DB_DETAILS['db_name'],
                                db_user = DB_DETAILS['db_user'],
                                db_pass = DB_DETAILS['db_pass'] ) 
    return conn

