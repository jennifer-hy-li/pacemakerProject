import psycopg2

class PacemakerDatabase():
    """Enables functionality to communicate with the pacemaker database.
    Functionality provided includes:
     * Connection to the database.
     * Build tables in the database.
     * Populate tables in the database.
     * Store data in the database.
     * Query and get results from the database."""

    __instance = None
    
    @staticmethod
    def get_instance():
        """This method is used to statically access the database singleton object."""
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
    def table_exists(self, table: str):
        """Determines if there are any tables exists in the database.
        Returns 1 if there are any tables, else returns 0."""
        try:
            self.make_connection()
            self.cursor.execute(f"SELECT exists(\
                                    SELECT  *\
                                    FROM    information_schema.tables\
                                    WHERE   table_name = '{table}'\
                                )")
            return self.cursor.fetchone()[0]
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    
    def create_and_populate(self):
        """Runs two SQL scripts to create and populate all necessary tables in the database.
        This creates 5 tables in total. The structure for this relational database can be
        viewed in the ER diagram in this same directory."""
        try:
            self.make_connection()
            self.cursor.execute(open("database/pacemaker_sql_files/create_tables.sql", "r").read())
            print("Created Tables.")
            self.cursor.execute(open("database/pacemaker_sql_files/populate_tables.sql", "r").read())
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
                open("database/pacemaker_sql_files/drop_tables.sql", "r").read()
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
    def get_all_account_parameters(self, username: str):
        """Get all parameters for all modes with their assigned values for this user."""
        try:
            self.make_connection()
            self.cursor.execute(f"SELECT  *\
                                FROM    accountparameters\
                                WHERE   user = '{username}';")
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def get_parameters(self, username: str = None, mode: str = None, parameter: str = None):
        """Get values, optionally restrict username and mode and parameter."""
        try:
            self.make_connection()
            if username != None and mode != None and parameter != None:
                self.cursor.execute(f"SELECT  *\
                                    FROM    accountparameters\
                                    WHERE   username = '{username}' and mode = '{mode}' \
                                            and parameter = '{parameter}';")
            elif username != None and mode != None:
                self.cursor.execute(f"SELECT  *\
                                    FROM    accountparameters\
                                    WHERE   username = '{username}' and mode = '{mode}';")
            elif username != None and parameter != None:
                self.cursor.execute(f"SELECT  *\
                                    FROM    accountparameters\
                                    WHERE   username = '{username}' and parameter = '{parameter}';")
            elif mode != None and parameter != None:
                self.cursor.execute(f"SELECT  *\
                                    FROM    accountparameters\
                                    WHERE   mode = '{mode}' and parameter = '{parameter}';")
            elif mode != None:
                self.cursor.execute(f"SELECT  *\
                                    FROM    modeparameters\
                                    WHERE   mode = '{mode}';")
            elif username != None:
                self.cursor.execute(f"SELECT  *\
                                FROM    accountparameters\
                                WHERE   username = '{username}';")
            elif parameter != None:
                self.cursor.execute(f"SELECT  *\
                                FROM    accountparameters\
                                WHERE   parameter = '{parameter}';")
            elif username == None and mode == None and parameter == None:
                self.cursor.execute(f"SELECT * FROM parameters;")
            else:
                raise Exception("get_parameters function is broken.")

            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def upsert_parameter_value(self, username: str, mode: str, parameter: str, value: float):
        """Update or insert a single parameter's value, for a given user, mode, and parameter.
        Note: If the primary key already exists, the value will be updated for the corresponding row.
        Otherwise, the row will be inserted. This is known as upsert."""
        try:
            self.make_connection()
            self.cursor.execute(f"INSERT INTO accountparameters\
                                VALUES ('{username}', '{mode}', '{parameter}', '{value}')\
                                ON CONFLICT (username, parameter, mode)\
                                DO UPDATE SET value = '{value}';")
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    # ------------------- ACCOUNT_PARAMETERS SQL QUERIES END --------------------- #

    # -------------------- MODE_PARAMETERS SQL QUERIES START --------------------- #
    def get_modes_from_modeparameters(self):
        """Gets all modes and parameters from the modeparameters table"""
        try:
            self.make_connection()
            self.cursor.execute(f"SELECT  *\
                                FROM    ModeParameters")
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def get_unique_modes_from_modeparameters(self):
        """Gets all unique modes from the modeparameters table"""
        try:
            self.make_connection()
            self.cursor.execute(f"SELECT DISTINCT mode\
                                FROM    ModeParameters")
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def get_default_parameter_value(self, mode: str, parameter: str):
        """Gets the default value assigned to one parameter from a particular mode."""
        try:
            self.make_connection()
            self.cursor.execute(f"SELECT  *\
                                FROM    modeparameters\
                                WHERE   mode = '{mode}' and parameter = '{parameter}';")
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()

    def set_default_parameter_value(self, mode: str, parameter: str, defaultValue: int):
        """Assign a default value to a parameter for a given mode."""
        try:
            self.make_connection()
            self.cursor.execute(f"UPDATE  modeparameter\
                                SET     mode = '{mode}',\
                                        parameter = '{parameter}',\
                                        defaultValue = '{defaultValue}'\
                                WHERE   mode = '{mode}' and\
                                        parameter = '{parameter}';")
            self.connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    # -------------------- MODE_PARAMETERS SQL QUERIES END ----------------------- #

    # ------------------------- MODES SQL QUERIES START -------------------------- #
    def get_all_modes(self):
        """Get all modes in the mode table."""
        try:
            self.make_connection()
            self.cursor.execute(f"SELECT * FROM mode;")
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error :
            print ("PostgreSQL error:", error)
        finally:
            self.close_connection()
    # -------------------------- MODES SQL QUERIES END --------------------------- #

