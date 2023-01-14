from sql_query.insert_table_query import song_table_insert, artist_table_insert

def extract_song(spark_session , cur, path) :

    """this function extract the song data from the song_data folder and insert the data into the song and artist table """
    # insert song record
    df = spark_session.read.json(path)
    song_data = tuple((df.select(['song_id', 'title', 'artist_id', 'year', 'duration']).collect()[0]))
    cur.execute(song_table_insert, song_data)
    print('-----------------------------------ok-------------------------------------')

    # insert artist record
    df = spark_session.read.json(path)
    song_data = tuple((df.select(['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']).collect()[0]))
    cur.execute(artist_table_insert, song_data)

