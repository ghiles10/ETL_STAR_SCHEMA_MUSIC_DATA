from pyspark.sql import SparkSession


def spark_session(): 

    """Create a spark session to run the ETL pipeline. 
    Returns: 
        spark_session: Spark session object. 
    """ 
    
    session = SparkSession.builder.appName('ETL').getOrCreate() 

    return session
    