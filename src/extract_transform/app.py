import sys
import os

sys.path.append(r'./src')
sys.path.append(r'.')

if not os.path.exists("./log"):
    os.mkdir("log")

from extract_all import main_extract_data 
from sql_query.create_table import main_create_table 

if __name__ == "__main__":
    main_create_table()
    main_extract_data()

   