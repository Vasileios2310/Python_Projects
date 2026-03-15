import mysql.connector
from mysql.connector import Error

def create_connection(host_name , user_name , user_password):
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )
        print("Connection to MySQL DB successfully")
    except Error as ex:
        print(f"Error : '{ex}' occured")
        
    return connection

def create_database (connection , query):
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as ex:
        print(f"Error : '{ex}' occured")
    finally:
        cursor.close()
        
def main():
    conn = create_connection('localhost' , 'root' , 'password')
    if conn:
        create_database_query = "CREATE DATABASE pythonDB"
        create_database(conn , create_database_query)
        conn.close()
        print("MySQL conncection closed")
    
    
if __name__ == '__main__':
    main()