# Authors: Jayden Hooper, Jennifer Li

class indicateConnection():
    def __init__(self, connection_status: bool):
        self.__connection_status = connection_status
        self.update_connection()

    def update_connection(self):
        if self.__connection_status:
            self.__connection_label = "Pacemaker Connected"
            self.__color = "green"
        else:
            self.__connection_label = "Pacemaker Disconnected"
            self.__color = "red"

    def set_connection_status(self, status):
        self.__connection_status = status

    def get_connection_status(self):
        return self.__connection_status

    def get_color(self):
        return self.__color
    
    def get_connection_label(self):
        return self.__connection_label
    