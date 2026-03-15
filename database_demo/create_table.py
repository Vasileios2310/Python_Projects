import mysql.connector
from mysql.connector import Error


def create_connection(host_name , user_name , user_password, db_name , port):
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name,
            port = port
        )
        
        print("Connection to MySQL Db successfully")
    except Error as ex:
        print(f"Error {ex}")
    return connection
    
def create_tables(connection):
    create_table_teachers = """
    CREATE TABLE IF NOT EXISTS teachers(
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50),
        age INTEGER
    )
    """
    create_table_students = """
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50)
    )
    """
    
    cursor = connection.cursor()
    try:
        cursor.execute("BEGIN")
        cursor.execute(create_table_teachers)
        cursor.execute(create_table_students)
        connection.commit()
        print("Tabels created successfully")
    except Error as ex:
        print(f"Error {ex} occured")
        connection.rollback()
    finally:
        cursor.close()
        
def main():
    conn = create_connection('localhost' , 'root' , 'password', 'pythonDB' , 3306)
    if conn:
        create_tables(conn)
        conn.close()
        print("MySQL conncection closed")
    
    
if __name__ == '__main__':
    main()