import tkinter as tk
from Windows import *
from database.PacemakerDatabase import *

def main():
    """The main function is responsible for setting up and running the program."""
    db = PacemakerDatabase.get_instance()
    if not db.table_exists('account'):
        db.create_and_populate()
    x = db.get_all_account_parameters('123')
    print(x)
    MainWindow(tk.Tk())
    tk.mainloop()

if __name__ == '__main__':
    main()