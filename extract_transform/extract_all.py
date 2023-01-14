import sys
sys.path.append(r'/workspaces/AIRFLOW_MUSIC')
import os
from extract_song_artist import extract_song 
from extact_user_infos_fact_table import extract_user_time_fact_table
from utils.utils import spark_session, connection_object

def extract_to_postgres(spark_ses, cur, conn, type_file) : 
    
    """ this function extract data from the song_data and log_data folder and insert them into the database"""
    
    path_dir = '/workspaces/AIRFLOW_MUSIC/data/'
    for root, _ , file in os.walk(f"{path_dir} + {type_file}"):
        for f in file: 
            path_data = str(os.path.join(root, f))  
                   
            if type_file == 'song_data' : 
                extract_song(spark_ses , cur, path_data)
                conn.commit() 
                
            elif type_file == 'log_data' :
                extract_user_time_fact_table(spark_ses , cur, path_data)
                conn.commit()                  
                
def main() : 
    
    """ this function call the extract_to_postgres function"""
    spark = spark_session()
    conn = connection_object()
    cur = conn.cursor()
    
    extract_to_postgres(spark, cur, conn, 'song_data')
    extract_to_postgres(spark, cur, conn, 'log_data')
    
if __name__ == "__main__" : 
    main()