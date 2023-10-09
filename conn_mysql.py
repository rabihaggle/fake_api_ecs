import mysql.connector
from decouple import Config, Csv

def checkstatusbd(db_host,db_user,db_password,db_name):
    try:

        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        if conn.is_connected():
            return True, "True"
        else:
            return False, "Not Exception"
    
    except Exception as e:
        return False, str(e) 
    finally:
         if 'conn' in locals():
            conn.close()
    