# Music Data ETL

This repository houses an ETL pipeline that processes music data sourced from a music application. The pipeline retrieves data from logs and files, transforms it, and loads it into a star schema in a PostgreSQL database 

The main objective of this database is to provide the music app with a reliable and consistent source of data that can be used to answer various business questions related to the music preferences and habits of its users. By leveraging the data stored in logs and files, this database allows to gain insights into the types of songs and artists that are popular among its users 

## Data Retrieval
Data is retrieved from JSON files using file reading with PySpark.

## Data Transformation
Data is then transformed using PySpark to clean, format, and normalize the data.

## Database Design
Finally, the data is loaded into a PostgreSQL database using a star schema for improved query performance.

## Execution 
To execute the ETL pipeline, you must have PySpark and PostgreSQL dependencies installed.

Create a .env file : 

```
# postgres 
DB_NAME=database
DB_USER=user
DB_PASS=password
```

Enter this command : 
```
Make run 
```
