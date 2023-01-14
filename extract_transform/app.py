import sys
sys.path.append(r'./')

from extract_all import main_extract_data 
from sql_query.create_table import main_create_table 



if __name__ == "__main__":
    main_create_table()
    main_extract_data()
   
    
    

