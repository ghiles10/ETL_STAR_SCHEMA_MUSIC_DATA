def format_datetime(ts):
    
    """this function converts a timestamp to a datetime object """ 
    import datetime
    return datetime.datetime.fromtimestamp(ts/1000.0)



from pyspark.sql.types import DateType , TimestampType 
from pyspark.sql.functions import udf
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, dayofweek

# create timestamp column from original timestamp column
get_timestamp = udf(lambda x: format_datetime(int(x)), TimestampType())
df = df.withColumn("start_time", get_timestamp(df.ts))

# create datetime column from original timestamp column
get_datetime = udf(lambda x: format_datetime(int(x)), DateType())
df = df.withColumn("datetime", get_datetime(df.ts))

# extract columns to create time table
time_table = df.select( 'start_time', 'datetime' , 
                        hour("datetime").alias('hour'),
                        dayofmonth("datetime").alias('day'),
                        weekofyear("datetime").alias('week'),
                        year("datetime").alias('year'),
                        month("datetime").alias('month'),
                        dayofweek("datetime").alias('weekday') )


                        