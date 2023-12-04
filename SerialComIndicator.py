
connection_status=0

class indicateConnection():
    def __init__(self, Color,connectionLabel):        
        self.Color=Color
        self.connectionLabel=connectionLabel
    def check_connection(self):
        global connection_status
        if connection_status:
            self.connectionLabel="Pacemaker Connected"
            self.Color="green"
        else:
            self.connectionLabel="Pacemaker Disconnected"
            self.Color="red"

def set_global_connection_status(status):
    global connection_status
    connection_status = status
    print('in')

        # check_connection.connection_status = connection_status
        # self.master.after(1000, check_connection)
    # def update_circle(self):

        # canvas.delete("connection_circle")  # Delete existing circles

        # x1, y1, x2, y2 = 2, 2, 18, 18

        # # Draw the circle
        # canvas.create_oval(x1, y1, x2, y2, fill=color, tags="connection_circle")