from sql_query.insert_table_query import song_table_insert, artist_table_insert
import logging

def extract_song(spark_session , cur, path) :

    """this function extract the song data from the song_data folder and insert the data into the song and artist table """
    
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler('log/create_tables.log', mode = 'w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(module)s  - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    # insert song record
    df = spark_session.read.json(path)
    song_data = tuple((df.select(['song_id', 'title', 'artist_id', 'year', 'duration']).collect()[0]))
    cur.execute(song_table_insert, song_data)
    
    logger.info('song table extracted')

    # insert artist record
    df = spark_session.read.json(path)
    song_data = tuple((df.select(['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']).collect()[0]))
    cur.execute(artist_table_insert, song_data)

    logger.info('artist table extracted')
