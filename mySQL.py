import psycopg2

def start_connection():
    try:
        connection = psycopg2.connect(user = "postgres",
                                    password = "password",
                                    host = "localhost",
                                    port = "5432",
                                    database = "postgres")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM account")
        print(cursor.fetchone())

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        close_connection(connection, cursor)


def make_new_user(username: str, password: str):
    pass

def close_connection(connection, cursor):
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
    
start_connection()