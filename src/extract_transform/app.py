import sys
import os
sys.path.append(r'./src')
sys.path.append(r'.')
from extract_all import main_extract_data 
from sql_query.create_table import main_create_table 


if not os.path.exists("./src/log"):
    os.mkdir("./src/log")

if __name__ == "__main__":
    main_create_table()
    main_extract_data()

   