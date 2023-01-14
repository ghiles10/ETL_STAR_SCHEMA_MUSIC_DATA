from preprocess_time import table_time
from utils.utils import  insert
from fact_table import extract_fact_table
from sql_query.insert_table_query import user_table_insert, time_table_insert
def extract_user_time_fact_table(spark_session , cur, path):
    
    # open log file
    df = spark_session.read.json(str(path))

    # filter by NextSong action
    df = df.filter(df["page"] == "NextSong")
    
    # add time table 
    time_table = table_time(df)
    insert(time_table, cur, time_table_insert)
    
    print('-----------time SQL table ok-----------')
    
    # load user table
    user_df = df.select(['userId', 'firstName', 'lastName', 'gender', 'level']) 
    # insert user records
    insert(user_df, cur, user_table_insert)     
    
    print('-----------user SQL table ok-----------')

    # insert songplay records fact table 
    extract_fact_table(df , cur)
    print('-----------fact SQL table ok-----------')

    
    