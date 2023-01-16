import os
from extract_song_artist import extract_song 
from extact_user_infos_fact_table import extract_user_time_fact_table
from utils.utils import spark_session, connection_object
import logging

logger = logging.getLogger(__name__)
handler = logging.FileHandler('log/create_tables.log', mode = 'w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(module)s  - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def extract_to_postgres(spark_ses, cur, conn, type_file, logger = logger) : 
    
    """ this function extract data from the song_data and log_data folder and insert them into the database"""
    path_dir = './data/'
    
    
    count = 0  
    for root, _ , file in os.walk(f"{path_dir}{type_file}"):
        for f in file:
            count += 1
            print("fichier json numro", count,type_file )
            
            path_data = str(os.path.join(root, f))  
                
            if type_file == 'song_data' : 
                extract_song(spark_ses , cur, path_data)
                conn.commit() 

            elif type_file == 'log_data' :
                extract_user_time_fact_table(spark_ses , cur, path_data)

                conn.commit()                  
            
def main_extract_data(logger = logger) : 
    
    """ this function call the extract_to_postgres function"""
    spark = spark_session()
    conn = connection_object()
    cur = conn.cursor()
    
    print('song data begin')
    extract_to_postgres(spark, cur, conn, 'song_data')
    logger.info('song data extracted')

    print('log data begin') 
    extract_to_postgres(spark, cur, conn, 'log_data')
    logger.info('log data extracted')

    
if __name__ == "__main__" : 
    main_extract_data()