import tkinter as tk
from LoginPage import Loginpage

class MainWindow():
    def __init__(self, master):
        mainframe = tk.Frame(master)
        mainframe.pack(padx=10,pady=10,fill='both',expand=1)

        # Initial frame
        Home(mainframe)

class Home(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text = "Pacemaker v0 0.1.0", font=("Arial", 22)).grid(
            row=10, column=10, sticky=tk.W + tk.E, columnspan=10, pady=2)
        tk.Label(self, text = "Welcome [User]", font=("Arial", 12)).grid(
            row=20, column=10, sticky=tk.W + tk.E, columnspan=10, pady=(0,50))
        
        # Device label with status
        tk.Label(self, text = "Device", font=("Arial", 16)).grid(
            row=30, column=10, padx = (0,20))
        tk.Label(self, text = "Status + DeviceID", font=("Arial", 12)).grid(
            row=40, column=10)
        
        # Mode with drop down menu, help hover, and submit button
        tk.Label(self, text = "Mode", font = ("Arial", 16)).grid(
            row=30, column=11, padx = (20,0))
        # Building the drop down menu
        modeList = tk.StringVar(self)  
        modeList.set("Please Select...")
        optionsList = ["AOO", "VOO", "AAI", "VVI"]
        options = tk.OptionMenu(self, modeList, *optionsList)
        options.grid(row=40, column=11, padx = (20,0))
        submit_button = tk.Button(self, text='Submit', 
                                  command=lambda: self.submit(modeList.get()))
        submit_button.grid(row = 40, column = 12)
        sign_in_button = tk.Button(self, text="Sign In", 
                                   command=lambda: (self.destroy(), SignIn(parent)))
        sign_in_button.grid(row=50, column=10, columnspan=10, pady=(50,0))

        # sign_up_button = tk.Button(self.bottomframe, text="Sign Up", 
        #                            command=lambda: (initialFrame.destroy(), SignUp(mainframe)))
        # sign_up_button.pack(padx=10,pady=10)
        # help hover
        
        self.pack(padx=100,pady=100)
    
    def submit(self, option: str):
        print(option)

class SignIn(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        signInWindow=tk.Frame(self, bg="white", width="500", height="500" )
        signInWindow.pack()
        self.pack(padx=0,pady=0)

        Loginpage(self)#self passed into Loginpage as root window
        

class SignUp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="SignUp Page (TODO)").pack(padx=10,pady=10)
        sign_in_button = tk.Button(self, text="Sign In", 
                                     command=lambda: (self.destroy(), SignIn(parent)))
        sign_in_button.pack(padx=10,pady=10)
        self.pack(padx=10,pady=10)


MainWindow(tk.Tk())
tk.mainloop()