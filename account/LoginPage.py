# Author: Jennifer Li

# login_module.py

from tkinter import *
from tkinter import messagebox
from database.PacemakerDatabase import PacemakerDatabase
from account.RegisterPage import registerPage
#from SerialComIndicator import set_global_connection_status
windowUsername = "[User]"


class LoginPage:
    

    def __init__(self, master):
        self.my_frame = master
        self.user_database = PacemakerDatabase.get_instance()

        #set_global_connection_status(1)

         # Define widgets as class attributes
        self.frame = Frame(self.my_frame, width=350, height=350, bg="white")
        self.heading = Label(self.frame, text="Sign in", fg='#57a1f8', bg="white", font=('Microsoft Yahei UI Light', 23, 'bold'))
        self.user = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.code = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))

        self.create_login_page()

    def create_login_page(self):
        self.frame.place(x=70, y=70)


        #self.heading=Label(self.frame, text="Sign in", fg='#57a1f8', bg="white", font=('Microsoft Yahei UI Light', 23,'bold'))
        self.heading.place(x=100, y=5)

        ######## user -----------------------

        # #event functions
        # def on_enter(e):
        #     user.delete(0, 'end')

        # def on_leave(e):
        #     name=user.get()
        #     if name=='':
        #         user.insert(0, 'Username')


        #user textbox
        #self.user = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0,'Username')

        # Event listeners
        self.user.bind('<FocusIn>', self.on_user_entry_focus_in)
        self.user.bind('<FocusOut>', self.on_user_entry_focus_out)

        #textbox lines
        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=107)

        ######## passoword -------------------
        # #event functions
        # def on_enter(e):
        #     code.delete(0, 'end')

        # def on_leave(e):
        #     name=code.get()
        #     if name=='':
        #         code.insert(0, 'Password')


        #self.code = Entry(self.frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0,'Password')

        #event listeners
        self.code.bind('<FocusIn>', self.on_code_entry_focus_in)
        self.code.bind('<FocusOut>', self.on_code_entry_focus_out)

        Frame(self.frame, width=295, height=2, bg='black').place(x=25, y=177)

        ########## sign in button ----------
        #command=sign in for login verification
        Button(self.frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=self.signin).place(x=35, y=204)
        label=Label(self.frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light',9))
        label.place(x=40, y=270)

        label=Label(self.frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light',9))
        label.place(x=40, y=270)
        sign_up=Button(self.frame, width=6, text="Sign up", border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda:self.openRegister())
        sign_up.place(x=200, y=270)
        self.my_frame.mainloop()

    def signin(self):
        username = self.user.get()
        password = self.code.get()

        if self.user_database.user_exists(username):
            if self.user_database.get_password(username) == password:
                
                global windowUsername
                windowUsername = username
                #set_global_connection_status(0)
               
                self.frame.quit()
                self.my_frame.destroy()
                return
            else:
                messagebox.showerror("Invalid", "Invalid password")
        else:
            messagebox.showerror("Invalid", "Invalid username. Register using the sign-up button below.")

    def openRegister(self):
        register_window = Toplevel(self.my_frame)
        register_window.title("Registration")
        register_window.geometry('500x500')
        registerPage(register_window)
       

    # Event functions
    def on_user_entry_focus_in(self, event):
        self.user.delete(0, 'end')

    def on_user_entry_focus_out(self, event):
        name = self.user.get()
        if name == '':
            self.user.insert(0, 'Username')

    def on_code_entry_focus_in(self, event):
        self.code.delete(0, 'end')

    def on_code_entry_focus_out(self, event):
        name = self.code.get()
        if name == '':
            self.code.insert(0, 'Password')

   
def getUser():
    return windowUsername

