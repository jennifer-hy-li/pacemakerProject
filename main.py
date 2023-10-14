import tkinter as tk
from Windows import *
from database.PacemakerDatabase import *

def main():
    db = PacemakerDatabase()
    if not db.table_exists('account'):
        db.create_and_populate()
    MainWindow(tk.Tk())
    tk.mainloop()

if __name__ == '__main__':
    main()