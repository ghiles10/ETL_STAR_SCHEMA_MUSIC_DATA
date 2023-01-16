from pyspark.sql.types import DateType , TimestampType, NumericType	
from pyspark.sql.functions import udf
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, dayofweek
import datetime

def table_time(df) :

    """this function extracts the time table from the json file and returns a dataframe"""
    
    def format_datetime(ts):
        
        """this function converts a timestamp to a datetime object """ 
        return datetime.datetime.fromtimestamp(ts/1000.0)


    # create datetime column from original timestamp column
    get_datetime = udf(lambda x: format_datetime(int(x)), DateType())
    df = df.withColumn("datetime", get_datetime(df.ts))

    # extract columns to create time table
    time_table = df.select( 'ts' , 
                            hour("datetime").alias('hour'),
                            dayofmonth("datetime").alias('day'),
                            weekofyear("datetime").alias('week'),
                            month("datetime").alias('month'),
                            year("datetime").alias('year'),
                            dayofweek("datetime").alias('weekday') )

    
    print('-----------time table ok-----------')
    return time_table

                        