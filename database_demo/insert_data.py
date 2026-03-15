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

def insert_teacher(connection , teacher):
    cursor = connection.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO teachers (id , firstname , lastname , age) VALUES (%s , %s , %s , %s)",
            teacher
        )
        connection.commit()
        print("Teacher inserted successfully")
    except Error as ex:
        print(f"Error {ex}")
        connection.rollback()
    finally:
        connection.close()
           
def main():
    conn = create_connection('localhost' , 'root' , 'password', 'pythonDB' , 3306)
    if conn:
        teacher = (1 , "Alice" , "W." , 30)
        insert_teacher(conn , teacher)
        conn.close()
        print("MySQL conncection closed")
    
    
if __name__ == '__main__':
    main()