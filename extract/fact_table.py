def extract_fact_table( df , cur):                                      
                                                                   
    """this function extracts the fact table from the json file and returns a dataframe """
                                                           
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
        
        