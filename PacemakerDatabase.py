import psycopg2

class PacemakerDatabase():

    def __init__(self, user = "postgres", password = "theLih0me!", 
                 host = "localhost", port = "5432", database = "pacemaker"):
        """This constructor allows you to modify the server connection details if necessary."""
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def make_connection(self):
        """Helper function to connect to SQL database"""
        self.connection = psycopg2.connect(user = self.user,
                                    password = self.password,
                                    host = self.host,
                                    port = self.port,
                                    database = self.database)
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
        """Get all user data, given a username"""
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

    def get_password(self, username: str):
        """Get all user password, given a username"""
        try: 
            self.make_connection()
            self.cursor.execute(f"SELECT  password\
                                 FROM    account\
                                 WHERE   username = '{username}'")
            returnPassword=self.cursor.fetchone()[0]
            return returnPassword
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    
    def user_exists(self, username: str):
        """Returns whether user exists, given a username"""
        try: 
            self.make_connection()
            self.cursor.execute(f"SELECT COUNT(username) FROM account WHERE username = '{username}'")
            existance =self.cursor.fetchone()[0]
            return existance #returns value whether user exists 1 exists, 0 doesn't exist
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    
    def get_user_count(self):
        """Returns whether user exists, given a username"""
        try: 
            self.make_connection()
            self.cursor.execute(f"SELECT COUNT(username) FROM account")
            count =self.cursor.fetchone()[0]
            print(count)
            print(type(count))
            return count #returns value whether user exists 1 exists, 0 doesn't exist
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

    def create_account_table(self):
        """Creates the account table with a trigger to limit the rows to 10."""
        try:
            self.make_connection()
            self.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS account (\
                username VARCHAR (50) UNIQUE NOT NULL,\
                password VARCHAR (50) NOT NULL CONSTRAINT \"Password length must be between 3 and 50\"\
                CHECK(length(password) >= 3 AND length(password) <= 50));\
                \
                CREATE OR REPLACE FUNCTION check_number_of_rows()\
                RETURNS TRIGGER AS\
                $body$\
                BEGIN\
                    IF (SELECT count(*) FROM account) >= 10\
                    THEN\
                        RAISE EXCEPTION 'Cannot add an additional user, as the 10 user limit has been reached.';\
                    END IF;\
                    RETURN NEW;\
                END;\
                $body$\
                LANGUAGE plpgsql;\
                \
                CREATE OR REPLACE TRIGGER tr_check_number_of_rows\
                BEFORE INSERT ON account\
                FOR EACH ROW EXECUTE PROCEDURE check_number_of_rows();")
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def drop_account_table(self):
        """WARNING: Drops the entire account table and all data associated with it"""
        try:
            self.make_connection()
            self.cursor.execute(f"DROP TABLE IF EXISTS account;")
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

database = PacemakerDatabase()
database.create_account_table()
database.add_user("Jay", "jaysPassword") #tester for login, already registered users
database.add_user("admin", "1234")
database.get_all_users()
database.get_user_count()
#database.drop_account_table()

#pass database object to other modules
def passDatabase():
    return database

# # Test commands
# database = PacemakerDatabase()
# database.create_account_table()
# for i in range(5):
#     database.add_user(f"user{i}", "password")
# database.get_all_users()
# database.add_user("Jay", "jaysPassword")
# database.get_all_users()
# database.delete_user("Jay")
# database.get_all_users()
# database.get_user("user1")
# for i in range(5):
#     database.add_user(f"user{i+5}", "password")
# database.get_all_users()
# print("expecting 10 user limit error for next operation:")
# database.add_user("user11", "password")
# print("make sure program still works:")
# database.get_all_users()
# database.drop_account_table()