import psycopg2

class PacemakerDatabase():

    __instance = None

    @staticmethod
    def get_instance():
        """Static access method"""
        if PacemakerDatabase.__instance == None:
            PacemakerDatabase()
        return PacemakerDatabase.__instance

    def __init__(self, user = "postgres", password = "password", 
                 host = "localhost", port = "5432", database = "postgres"):
        """This constructor allows you to modify the server connection details if necessary."""
        if PacemakerDatabase.__instance != None:
            raise Exception("Cannot instantiate more than one instance. Use get_instance()")
        PacemakerDatabase.__instance = self
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def modify_connection_arguments(self, user = "postgres", password = "password", 
                                    host = "localhost", port = "5432", database = "postgres"):
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

        
