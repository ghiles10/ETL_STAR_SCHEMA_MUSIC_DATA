def process_log_file(spark_session , cur, path):
     
    # open log file
    df = spark_session.read.json(str(path))

    # filter by NextSong action
    df = df.filter(df["page"] == "NextSong")
