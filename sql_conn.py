import pandas as pd
import mysql.connector
from mysql.connector import Error
import datetime
import random
import sys

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',            # host may be local or remote, In case of Remote 'Ip:port'
                                       database='sql_store',        #  Give your database Name
                                       user='db_user_name',         # Data Base User
                                       password='db_user_password') # Database password
        if conn.is_connected():
            print('Connected to MySQL database\n')
# Give your sql queary below  within ''' your sql  query goes here'''
            sql_query = pd.read_sql_query(''' 
                              your sql query goes here                       
                              '''
                                        ,conn)

            filename = datetime.datetime.now().strftime("Sql_Dump_%Y_%m_%d-%H%M%S")
            df = pd.DataFrame(sql_query)
            df.to_csv (r'C:\Users\{}.csv'.format(filename)) # Give your dump path
            print ("Dump has been  Successfully fetched.")

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()




if __name__ == '__main__':
    connect()
