# Authors: Jayden Hooper, Jennifer Li

from abc import abstractmethod

class Indicator():
    """This class is responsible for the serial communication indicator."""

    __instance = None

    @staticmethod
    def get_instance():
        """This method is used to statically access the database singleton object."""
        if Indicator.__instance == None:
            Indicator()
        return Indicator.__instance

    def __init__(self):
        """Initializes the connection status and updates the connection label."""
        if Indicator.__instance != None:
            raise Exception("Cannot instantiate more than one instance. Use get_instance()")
        Indicator.__instance = self
        self.__connection_status = 0
        self.__connection_label = "Pacemaker Not Communicating"
        self.__color = "red"
        self.subscribers = []

    def update_connection(self):
        """Updates the connection label and color based on the connection status."""
        if self.__connection_status:
            self.__connection_label = "Pacemaker Communicating"
            self.__color = "green"
        else:
            self.__connection_label = "Pacemaker Not Communicating"
            self.__color = "red"
        
        self.notify_subscribers()

    def set_connection_status(self, status):
        """Sets the connection status."""
        self.__connection_status = status
        self.update_connection()

    def get_connection_status(self):
        """Returns the connection status."""
        return self.__connection_status

    def get_color(self):
        """Returns the color of the indicator."""
        return self.__color
    
    def get_connection_label(self):
        """Returns the connection label."""
        return self.__connection_label
    
    def subscribe(self, subscriber):
        """Adds a subscriber to the indicator."""
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        """Removes a subscriber from the indicator."""
        self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        """Notifies all subscribers of a change."""
        for subscriber in self.subscribers:
            subscriber.update_indicator()

class Subscriber():
    """Responsible for updating the connection label and color."""

    def __init__(self):
        """Initializes the subscriber."""
        self.indicator = Indicator.get_instance()
        self.indicator.subscribe(self)

    @abstractmethod
    def update_indicator(self):
        """For the subscriber to implement."""
        print("update() not implemented")
