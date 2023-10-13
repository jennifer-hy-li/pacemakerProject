from tkinter import *
from tkinter import messagebox
from database.PacemakerDatabase import PacemakerDatabase

def registerPage(mainWindow):
    userDatabase= PacemakerDatabase.get_instance()# will be passed in from login page later
    userDatabase.get_all_users()

    #####SIGN UP LOGIC HERE, activated on 'sign up' button press
    def signup():
        username=user.get()
        password=code.get()
        count=userDatabase.get_user_count()
        #Type conversion for count
        if count is None:
            count2 = 0
            print('0')
        else:
            count2= count
            print(str(count2))

        if (userDatabase.user_exists(username)): ##user already in data base
            messagebox.showerror("Invalid", "Username already taken.")
        elif(count2>=10):#too many users
            messagebox.showerror("Invalid", "Sorry, we've reached our maximum capacity of 10 users.", COMMAND=frame.quit())
            mainWindow.destroy()
            return
        else: #create new user in data base
            userDatabase.add_user(username, password)
            messagebox.showerror("Registered", "You're registered! Sign in to continue.", COMMAND=frame.quit())
            mainWindow.destroy()
            return


    frame=Frame(mainWindow, width=350, height=350, bg="white")
    frame.place(x=70, y=70)


    heading=Label(frame, text="Register", fg='#57a1f8', bg="white", font=('Microsoft Yahei UI Light', 23,'bold'))
    heading.place(x=100, y=5)

    ######## user -----------------------

    #event functions
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0, 'Username')


    #user textbox
    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0,'Username')

    #event listener
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    #textbox lines
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ######## passoword -------------------
    #event functions
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0, 'Password')


    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0,'Password')

    #event listeners
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ########## sign up button ----------
    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=204)

    mainWindow.mainloop()

    return
