import tkinter as tk
from Windows import *
from database.PacemakerDatabase import *
from egram import *

def main():
    """The main function is responsible for setting up and running the program."""
    db = PacemakerDatabase.get_instance()
    if not db.table_exists('account'):
        db.create_and_populate()
    e = egram()
    
    MainWindow(tk.Tk())
    tk.mainloop()

if __name__ == '__main__':
    main()
    