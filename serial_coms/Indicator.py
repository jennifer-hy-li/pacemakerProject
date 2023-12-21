# Authors: Jayden Hooper, Jennifer Li

class IndicateConnection():
    """This class is responsible for the serial communication indicator."""

    __instance = None

    @staticmethod
    def get_instance():
        """This method is used to statically access the database singleton object."""
        if IndicateConnection.__instance == None:
            IndicateConnection()
        return IndicateConnection.__instance

    def __init__(self, connection_status: bool):
        """Initializes the connection status and updates the connection label."""
        if IndicateConnection.__instance != None:
            raise Exception("Cannot instantiate more than one instance. Use get_instance()")
        IndicateConnection.__instance = self
        self.__connection_status = connection_status
        self.update_connection()

    def update_connection(self):
        """Updates the connection label and color based on the connection status."""
        if self.__connection_status:
            self.__connection_label = "Pacemaker Connected"
            self.__color = "green"
        else:
            self.__connection_label = "Pacemaker Disconnected"
            self.__color = "red"

    def set_connection_status(self, status):
        """Sets the connection status."""
        self.__connection_status = status

    def get_connection_status(self):
        """Returns the connection status."""
        return self.__connection_status

    def get_color(self):
        """Returns the color of the indicator."""
        return self.__color
    
    def get_connection_label(self):
        """Returns the connection label."""
        return self.__connection_label
    