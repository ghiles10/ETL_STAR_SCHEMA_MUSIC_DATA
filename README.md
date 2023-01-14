# Music Data ETL

This repository contains an ETL pipeline for retrieving, transforming, and loading music data from log and files. The data is sourced from a music application. 

The main objective of this database is to provide the music app with a reliable and consistent source of data that can be used to answer various business questions related to the music preferences and habits of its users. By leveraging the data stored in logs and files, this database allows to gain insights into the types of songs and artists that are popular among its users 

## Data Retrieval
Data is retrieved from JSON files using file reading with PySpark.

## Data Transformation
Data is then transformed using PySpark to clean, format, and normalize the data.

## Database Design
Finally, the data is loaded into a PostgreSQL database using a star schema for improved query performance.

## Execution 
To execute the ETL pipeline, you must have PySpark and PostgreSQL dependencies installed. Then run the main script app.py to start the pipeline.
