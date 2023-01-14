import os
from extract_song_artist import extract_song 
from extact_user_infos_fact_table import extract_user_time_fact_table
from utils.utils import spark_session, connection_object

def extract_to_postgres(spark_ses, cur, conn, type_file) : 
    
    """ this function extract data from the song_data and log_data folder and insert them into the database"""
    path_dir = '/workspaces/AIRFLOW_MUSIC/data/'
    
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
            
def main_extract_data() : 
    
    """ this function call the extract_to_postgres function"""
    spark = spark_session()
    conn = connection_object()
    cur = conn.cursor()
    
    print('song data begin')
    extract_to_postgres(spark, cur, conn, 'song_data')
    print('--------------------------------------------------etract song data ok-----------------------------------------------')

    print('log data begin') 
    extract_to_postgres(spark, cur, conn, 'log_data')
    print('--------------------------------------------------etract log data ok-----------------------------------------------')

    
if __name__ == "__main__" : 
    main_extract_data()