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

    # -------------------------- CONNECTION METHODS START -------------------------- #
    def modify_connection_arguments(self, user = "postgres", password = "password", 
                                    host = "localhost", port = "5432", database = "postgres"):
        """Allows a user to modify the postgres connection arguments."""
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def make_connection(self):
        """Helper function to connect to SQL database."""
        self.connection = psycopg2.connect(user = self.user,
                                    password = self.password,
                                    host = self.host,
                                    port = self.port,
                                    database = self.database)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        """Helper function to close an SQL connection."""
        if(self.connection):
            self.cursor.close()
            self.connection.close()
    # --------------------------- CONNECTION METHODS END --------------------------- #

    # -------------------------- GENERAL SQL QUERIES START ------------------------- #
    def create_and_populate(self):
        """Create all necessary tables in the database."""
        try:
            self.make_connection()
            self.cursor.execute(open("database\pacemaker_sql_files\create_tables.sql", "r").read())
            print("Created Tables.")
            self.cursor.execute(open("database\pacemaker_sql_files\populate_tables.sql", "r").read())
            print("Populated Tables.")
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    
    def drop_all_tables(self):
        """WARNING: Drops all tables in the database."""
        try:
            self.make_connection()
            self.cursor.execute(
                open("database\pacemaker_sql_files\drop_tables.sql", "r").read()
            )    
            self.connection.commit()      
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    # -------------------------- GENERAL SQL QUERIES END ------------------------- #

    # ------------------------- ACCOUNT SQL QUERIES START ------------------------ #
    def add_user(self, username: str, password: str):
        """Register a new user to the database, given a username and password."""
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
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def user_exists(self, username: str):
        """Returns int 1 if user exists, given a username"""
        try: 
            self.make_connection()
            self.cursor.execute(f"SELECT COUNT(username) FROM account WHERE username = '{username}'")
            existance = self.cursor.fetchone()[0]
            return existance #1 exists, 0 doesn't exist
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def get_password(self, username: str):
        """Get a user password, given a username"""
        try: 
            self.make_connection()
            self.cursor.execute(f"SELECT  password\
                                 FROM    account\
                                 WHERE   username = '{username}'")
            return self.cursor.fetchone()[0]
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    
    def get_user_count(self):
        """Returns the number (int) of registered users in database"""
        try: 
            self.make_connection()
            self.cursor.execute(f"SELECT COUNT(username) FROM account")
            count = self.cursor.fetchone()[0]
            print(count)
            return count # returns value whether user exists 1 exists, 0 doesn't exist
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
        
    def get_all_users(self):
        """Get all users from the account table."""
        try:
            self.make_connection()
            self.cursor.execute("SELECT * FROM account")
            print(self.cursor.fetchall())
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def delete_user(self, username):
        """Delete given user from the account table."""
        try:
            self.make_connection()
            self.cursor.execute(f"DELETE FROM account\
                                 WHERE username = '{username}';")
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    # -------------------------- ACCOUNT SQL QUERIES END ------------------------- #

    # ------------------ ACCOUNT_PARAMETERS SQL QUERIES START -------------------- #
    def get_all_account_parameters(user: str):
        """Get all parameters for all modes with their assigned values for this user."""
        # TODO:
        pass

    def get_all_parameters(user: str, mode: str):
        """Get all parameters with their assigned values, for this user and mode."""
        # TODO:
        pass

    def get_parameter_value(user: str, mode: str, parameter: str):
        """Get a parameter's value, given a user, mode, and parameter."""
        # TODO:
        pass

    def set_parameter_value(user: str, mode: str, parameter: str):
        """Set a single parameter's value, for a given user, mode, and parameter."""
        # TODO:
        pass
    # ------------------- ACCOUNT_PARAMETERS SQL QUERIES END --------------------- #

    # -------------------- MODE_PARAMETERS SQL QUERIES START --------------------- #
    def get_all_parameters(mode: str):
        """Get all parameters and values associated with the given mode."""
        # TODO:
        pass

    def get_default_parameter_value(mode: str, parameter: str):
        """Gets the default value assigned to one parameter from a particular mode."""
        # TODO:
        pass

    def set_default_parameter_value(mode: str, parameter: str, defaultValue: int):
        """Assign a default value to a parameter for a given mode."""
        # TODO:
        pass
    # -------------------- MODE_PARAMETERS SQL QUERIES END ----------------------- #

    # ------------------------ PARAMETER SQL QUERIES START ----------------------- #
    def get_all_parameters():
        """Get all parameters in the parameters table."""
        # TODO:
        pass
    # ------------------------ PARAMETER SQL QUERIES END ------------------------- #

    # ------------------------- MODES SQL QUERIES START -------------------------- #
    def get_all_modes():
        """Get all modes in the mode table."""
        # TODO:
        pass
    # -------------------------- MODES SQL QUERIES END --------------------------- #

