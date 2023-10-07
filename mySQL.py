import psycopg2


class PacemakerDatabase():
    def __init__(self):
        pass

    def make_connection(self):
        """Helper function to connect to SQL database"""
        self.connection = psycopg2.connect(user = "postgres",
                                    password = "password",
                                    host = "localhost",
                                    port = "5432",
                                    database = "postgres")
        self.cursor = self.connection.cursor()

    def close_connection(self):
        """Helper function to close an SQL connection"""
        if(self.connection):
            self.cursor.close()
            self.connection.close()

    def add_user(self, username: str, password: str):
        """Register a new user to the database, given a username and password"""
        try:
            self.make_connection()
            self.cursor.execute(f"INSERT INTO account VALUES ('{username}', '{password}');")
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def get_user(self, username: str):
        """Get a user, given a username"""
        try: 
            self.make_connection()
            self.cursor.execute(f"SELECT  *\
                                 FROM    account\
                                 WHERE   username = '{username}'")
            print(self.cursor.fetchall())
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
        
    def get_all_users(self):
        """Get all users from the account table"""
        try:
            self.make_connection()
            self.cursor.execute("SELECT * FROM account")
            print(self.cursor.fetchall())
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def delete_user(self, username):
        """Delete given user from the account table"""
        try:
            self.make_connection()
            self.cursor.execute(f"DELETE FROM account\
                                 WHERE username = '{username}';")
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
        
# Test commands
database = PacemakerDatabase()
database.get_all_users()
database.add_user("Jay", "jaysPassword")
database.get_all_users()
database.delete_user("Jay")
database.get_all_users()
database.get_user("user1")