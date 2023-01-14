from utils.utils import connection_object

def create_tables(conn, cur):
    
    """
    Create fact and dim tables in the database 
    """
    user_table_create = ("""
    CREATE TABLE users
    (user_id int PRIMARY KEY, 
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar);
    """)

    song_table_create = ("""
    CREATE TABLE songs
    (song_id varchar PRIMARY KEY, 
    title varchar,
    artist_id varchar,
    year int,
    duration float);
    """)
    
    artist_table_create = ("""
    CREATE TABLE artists
    (artist_id varchar PRIMARY KEY, 
    name varchar,
    location varchar,
    latitude float,
    longitude float);
    """)

    time_table_create = ("""
    CREATE TABLE time
    (start_time bigint PRIMARY KEY, 
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int);
    """)
    
    query_songplay_table_create = ("""
    CREATE TABLE songplays
    (songplay_id SERIAL PRIMARY KEY, 
    start_time bigint REFERENCES time(start_time) ON DELETE RESTRICT, 
    user_id int REFERENCES users(user_id) ON DELETE RESTRICT, 
    level varchar, 
    song_id varchar REFERENCES songs(song_id) ON DELETE RESTRICT, 
    artist_id varchar REFERENCES artists(artist_id) ON DELETE RESTRICT, 
    session_id int);
    """)
        
    for query in [user_table_create, song_table_create, artist_table_create, time_table_create, query_songplay_table_create]:
        cur.execute(query)  
        conn.commit()
    
def main():
    
    """ execute create_tables function """
    
    conn = connection_object()
    cur = conn.cursor()
    
    create_tables(conn, cur)
    conn.close()

if __name__ == "__main__":
    main()
    
