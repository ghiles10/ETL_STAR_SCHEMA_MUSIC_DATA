from dotenv import load_dotenv
import os
load_dotenv(r'./.env')

DB_DETAILS = {
            'db_name': os.getenv("DB_NAME"),
            'db_user': os.getenv("DB_USER"),
            'db_host': '0.0.0.0',
            'db_pass': os.getenv("DB_PASS")
}

print( os.getenv("DB_NAME"))