import tkinter as tk
import future_utility.UtilityFunctions as util
import future_utility.PrintedReports as reports
from egram import *
from account.LoginPage import *
from PacemakerMode import AOO,VOO,AAI,VVI
from database.PacemakerDatabase import *
from SerialComIndicator import *

class MainWindow():
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

        indicator=indicateConnection("red","Pacemaker Disconnected")

         #initial display, serial com indicator
        connection_label = tk.Label(self.master, text=indicator.connectionLabel, fg=indicator.Color)
        connection_label.pack(pady=10, side=LEFT)

        canvas = tk.Canvas(self.master, width=20, height=20)
        canvas.create_oval(2, 2, 18, 18, fill=indicator.Color, tags="connection_circle")
        canvas.pack(side=LEFT)
        def update():
            connection_label.config(text=indicator.connectionLabel, fg=indicator.Color)
            canvas.delete("connection_circle")
            canvas.create_oval(2,2,18,18, fill=indicator.Color, tags="connection_circle")

        # self.master.after(100, indicator.check_connection)#repeatedly checks for connection
        # self.master.after(100, update)

        # set_global_connection_status(1)
        # Set up periodic check for the indicator
        self.check_indicator(indicator, update)

        # Initial frame
        SignIn(mainframe)

    def check_indicator(self, indicator, update_function):
        # Check the indicator every 1000 milliseconds (1 second)
        self.master.after(1000, self.check_indicator, indicator, update_function)

        # Perform the indicator check and update
        indicator.check_connection()
        update_function()

    def add_menubar(self):
        """Adds the menubar to the master frame. This provides options such as File, Settings, and Reports menus."""
        self.menubar = tk.Menu(self.master)
        self.master.config(menu = self.menubar)

        # add File to menubar
        self.file_menu = tk.Menu(self.menubar, bg = "white", tearoff = 0)
        self.menubar.add_cascade(menu = self.file_menu, label = "File")
        self.file_menu.add_cascade(label = "Home", command = lambda: (destroy_all_widgets(self.mainframe), Home(self.mainframe)))
        self.file_menu.add_command(label = "Sign Out", command = lambda: sign_out(self.mainframe))
        self.file_menu.add_command(label = "Quit", command = exit)

        # add Settings to menubar
        self.settings_menu = tk.Menu(self.menubar, bg = "white", tearoff = 0)
        self.menubar.add_cascade(menu = self.settings_menu, label = "Settings")
        self.settings_menu.add_command(label = "Set Clock", command = util.set_clock)

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
        if   selected_mode == "AOO":
            AOO(parent)
        elif selected_mode == "VOO":
            VOO(parent)
        elif selected_mode == "AAI":
            AAI(parent)
        elif selected_mode == "VVI":
            VVI(parent)

class SignIn(tk.Frame):
    """Frame to sign a user in, given a username and password."""
    def __init__(self, parent):
        super().__init__(parent)

        parent.main.hide_menubar()

        signInWindow=tk.Frame(self, bg="white", width="500", height="500" )
        signInWindow.pack()
        self.pack(padx=0,pady=0)

        #Loginpage(self) # self passed into Loginpage as root window
        login_page = LoginPage(self)

        
        
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
