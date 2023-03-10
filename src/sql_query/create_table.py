import sys
sys.path.append(r'.')
import logging

from utils.utils import connection_object

def create_tables(conn, cur):
       
    """
    Create fact and dim tables in the database 
    """
    
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler('log/create_tables.log', mode = 'w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(module)s  - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (user_id int PRIMARY KEY, 
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar);
    """)

    logger.info('user SQL table ok')

    song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs
    (song_id varchar PRIMARY KEY, 
    title varchar,
    artist_id varchar,
    year int,
    duration float);
    """)
    
    logger.info('song SQL table ok')
    
    artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists
    (artist_id varchar PRIMARY KEY, 
    name varchar,
    location varchar,
    latitude float,
    longitude float);
    """)

    time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (start_time BIGINT  PRIMARY KEY, 
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int);
    """)
    
    query_songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
    (songplay_id SERIAL PRIMARY KEY, 
    start_time BIGINT REFERENCES time(start_time) ON DELETE RESTRICT, 
    user_id int REFERENCES users(user_id) ON DELETE RESTRICT, 
    level varchar, 
    song_id varchar REFERENCES songs(song_id) ON DELETE RESTRICT, 
    artist_id varchar REFERENCES artists(artist_id) ON DELETE RESTRICT, 
    session_id int);
    """)
        
    for query in [user_table_create, song_table_create, artist_table_create, time_table_create, query_songplay_table_create]:
        cur.execute(query)  
        conn.commit()
    
def main_create_table():
    
    """ execute create_tables function """
    
    conn = connection_object()
    cur = conn.cursor()
    
    create_tables(conn, cur)
    conn.close()

if __name__ == "__main__":
    main_create_table()
    
