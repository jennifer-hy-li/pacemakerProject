# Authors: Jayden Hooper, Jennifer Li, Angeline Segado

import tkinter as tk
from Egram import *
from account.LoginPage import *
from PacemakerMode import *
from database.PacemakerDatabase import *
from serial_coms.ComsIndicator import *

class MainWindow(Subscriber):
    """The MainWindow is responsible for holding subframes. 
    This class allows frames to be created and destroyed, 
    while still being held in the same space."""
    def __init__(self, master):
        self.master = master
        mainframe = tk.Frame(master, bg = "white")
        self.mainframe = mainframe
        mainframe.main = self
        mainframe.pack(fill='both', expand=1)
        master.title("Pacemaker v0 0.1.0")

        self.e = egram()
        self.add_menubar()
        self.init_indicator()
        
        # Initial frame
        SignIn(mainframe)
    
    def init_indicator(self):
        self.indicator = Indicator.get_instance()
        self.indicator.subscribe(self)

        # Initial display, serial com indicator
        self.connection_label = tk.Label(self.master, text=self.indicator.get_connection_label(), fg=self.indicator.get_color())
        self.connection_label.pack(pady=10, side=LEFT)

        self.indicator_canvas = tk.Canvas(self.master, width=20, height=20)
        self.indicator_canvas.create_oval(2, 2, 18, 18, fill=self.indicator.get_color(), tags="connection_circle")
        self.indicator_canvas.pack(side=LEFT)

    def add_menubar(self):
        """Adds the menubar to the master frame. This provides options such as File, and Reports menus."""
        self.menubar = tk.Menu(self.master)
        self.master.config(menu = self.menubar)

        # add File to menubar
        self.file_menu = tk.Menu(self.menubar, bg = "white", tearoff = 0)
        self.menubar.add_cascade(menu = self.file_menu, label = "File")
        self.file_menu.add_cascade(label = "Home", command = lambda: (destroy_all_widgets(self.mainframe), Home(self.mainframe)))
        self.file_menu.add_command(label = "Sign Out", command = lambda: sign_out(self.mainframe))
        self.file_menu.add_command(label = "Quit", command = exit)

        # add Reports to menubar
        self.reports_menu = tk.Menu(self.menubar, bg = "white", tearoff = 0)
        self.menubar.add_cascade(menu = self.reports_menu, label = "Reports")

        self.reports_menu.add_command(label = "Atrium Electrogram", command = lambda: self.e.display_atr_egram())
        self.reports_menu.add_command(label = "Ventricle Electrogram", command = lambda: self.e.display_vent_egram())

    def hide_menubar(self):
        """Hides the menubar on the master frame. 
        Use when it doesn't make sense to have a menubar for a particular frame."""
        self.master.config(menu = "")

    def show_menubar(self):
        """Shows the menubar on the master frame."""
        self.master.config(menu = self.menubar)

    def update_indicator(self):
        """Updates the serial communication indicator."""
        self.connection_label.config(text=self.indicator.get_connection_label(), fg=self.indicator.get_color())
        self.indicator_canvas.delete("connection_circle")
        self.indicator_canvas.create_oval(2,2,18,18, fill=self.indicator.get_color(), tags="connection_circle")
        # self.master.update_idletasks()
        self.master.update()

        
class Home(tk.Frame):
    """The Home class is the frame which welcomes the user after signing in, providing numerous options for the user."""
    def __init__(self, parent):
        super().__init__(parent, bg = "white")

        parent.main.show_menubar()

        #tkinter needs stringvar type for label variables
        WelcomeMessage="Welcome "+ getUser()+"!"
        WelcomeMessageVar=tk.StringVar(self,WelcomeMessage)

        tk.Label(self, text = "Pacemaker v0 0.1.0", bg = "white", font=("Arial", 22)).grid(
            row=10, column=10, sticky=tk.W + tk.E, columnspan=10, pady=2)
        tk.Label(self, textvariable=WelcomeMessageVar, bg = "white", font=("Arial", 12)).grid(
            row=20, column=10, sticky=tk.W + tk.E, columnspan=10, pady=(0,50))

        # Device label with status
        tk.Label(self, text = "Device", bg = "white", font=("Arial", 16)).grid(
            row=30, column=10, padx = (0,20))
        tk.Label(self, text = "Status + DeviceID", bg = "white", font=("Arial", 12)).grid(
            row=40, column=10)
        
        # Mode with drop down menu, help hover, and submit button
        tk.Label(self, text = "Mode", bg = "white", font = ("Arial", 16)).grid(
            row=30, column=11, padx = (20,0))
        # Building the drop down menu
        modeList = tk.StringVar(self)  
        modeList.set("Please Select...")
        db = PacemakerDatabase.get_instance()
        unique_modes_query = db.get_unique_modes_from_modeparameters()
        unique_modes = []
        for mode in unique_modes_query:
            unique_modes.append(mode[0])
        options = tk.OptionMenu(self, modeList, *unique_modes)
        options.grid(row=40, column=11, padx = (20,0))
        options.config(bg = "white")
        options["menu"].config(bg = "white")
        submit_button = tk.Button(self, bg = "white", fg = "black", text='Submit', 
                                  command=lambda: (self.destroy(), self.submit(modeList.get(), parent)))
        submit_button.grid(row = 40, column = 12)
        sign_out_button = tk.Button(self, bg = "white", fg = "black", text="Sign Out", 
                                   command=lambda: (self.destroy(), SignIn(parent)))
        sign_out_button.grid(row=50, column=10, columnspan=10, pady=(50,0))
        
        self.pack(padx=100,pady=100)
    
    def submit(self, selected_mode, parent):
        """Auxiliary function for the options pane to change the frame to the submitted option."""
        print(selected_mode)
        if   selected_mode == "AOO":
            ProcessMode(parent, AOO())
        elif selected_mode == "VOO":
            ProcessMode(parent, VOO())
        elif selected_mode == "AAI":
            ProcessMode(parent, AAI())
        elif selected_mode == "VVI":
            ProcessMode(parent, VVI())
        elif selected_mode == "AOOR":
            ProcessMode(parent, AOOR())
        elif selected_mode == "VOOR":
            ProcessMode(parent, VOOR())
        elif selected_mode == "AAIR":
            ProcessMode(parent, AAIR())
        elif selected_mode == "VVIR":
            ProcessMode(parent, VVIR())
        

class SignIn(tk.Frame):
    """Frame to sign a user in, given a username and password."""
    def __init__(self, parent):
        super().__init__(parent)

        parent.main.hide_menubar()

        signInWindow=tk.Frame(self, bg="white", width="500", height="500" )
        signInWindow.pack()
        self.pack(padx=0,pady=0)

        LoginPage(self)       
        
        Home(parent)
        
            
# --------- Helper functions ---------- #

def sign_out(parent):
    """Signs out the user by destroying any current frames and returning to the login screen."""
    for widgets in parent.winfo_children():
        widgets.destroy()
    SignIn(parent)
            
def destroy_all_widgets(parent):
    """Destroys all widgets on the parent frame."""
    for widgets in parent.winfo_children():
        widgets.destroy()
