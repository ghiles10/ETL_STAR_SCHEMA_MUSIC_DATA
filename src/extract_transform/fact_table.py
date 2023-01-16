from sql_query.insert_table_query import song_artist_select, songplay_table_insert
import logging

def extract_fact_table( df , cur):                                      
                                                                   
    """this function extracts the fact table from the json file and returns a dataframe """
    
    logger = logging.getLogger(__name__)
    handler = logging.FileHandler('src/log/create_tables.log', mode = 'w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(module)s  - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
                                                           
    for row in range(int( df.count()) ):               
                                                  
        # get songid and artistid from song and artist tables
        cur.execute(song_artist_select, tuple( df.select(['song', 'artist', 'length']).collect()[row]))
        results = cur.fetchone()                        
                                                                           
        if results:                                                      
            songid, artistid = results                                   
        else:                                                            
            songid, artistid = None, None                                         
                                                                                    
        # insert songplay record                                                       
        songplay_data = ( df.select('ts').collect()[row][0], df.select('userId').collect()[row][0], df.select('level').collect()[row][0],
                         songid, artistid, df.select('sessionId').collect()[row][0])
        
        cur.execute(songplay_table_insert, songplay_data)
        logger.info('facet table extracted')
        