import tkinter as tk

class AOO:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AOO Mode")
        self.root.geometry("600x400")
        tk.Label(self.root, text="Mode: AOO", font = ('Arial',20)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self.root, text="Atrium Paced | No chamber sensed | No response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(50,0),pady=(0,10))

        canvas = tk.Canvas(self.root,width=490, height=20)
        canvas.grid(row =0,column =0, padx=(100,0))

        #device communication status indicator
        canvas.create_oval((470,3,490,20) ,fill="blue")
        #new device approaching status indicator
        canvas.create_oval((440,3,460,20) ,fill="red")

        tk.Label(self.root, text="Parameters", font = ('Arial',15),fg="blue").grid(row = 4, column=0, padx=(0,450))
        tk.Label(self.root, text="• Lower rate limit",font = ('Arial',12)).grid(row = 5, column=0, padx=(0,450))
        tk.Label(self.root, text="• Upper rate limit",font = ('Arial',12)).grid(row = 6, column=0, padx=(0,450))
        tk.Label(self.root, text="• Atrial amplitude",font = ('Arial',12)).grid(row = 7, column=0, padx=(0,447))
        tk.Label(self.root, text="• Atrial pulse width",font = ('Arial',12)).grid(row = 8, column=0, padx=(0,443))

        tk.Label(self.root, text="Device:",font = ('Arial',10)).grid(row = 30, column=0, padx=(0,550),pady=(140,0))
        tk.Label(self.root, text="[Show status + Device ID]",font = ('Arial',9)).grid(row = 31, column=0, padx=(0,450),pady=(0,0))



    def run(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()

class VOO:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VOO Mode")
        self.root.geometry("600x400")
        tk.Label(self.root, text="MODE: VOO", font = ('Arial',20)).grid(row = 1, column=0, padx=(70,0))
        tk.Label(self.root, text="Ventrical Paced | No chamber sensed | No response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(70,0),pady=(0,10))
        
        canvas = tk.Canvas(self.root,width=490, height=20)
        canvas.grid(row =0,column =0, padx=(100,0))

        #device communication status indicator
        canvas.create_oval((470,3,490,20) ,fill="blue")
        #new device approaching status indicator
        canvas.create_oval((440,3,460,20) ,fill="red")

        tk.Label(self.root, text="Parameters", font = ('Arial',15),fg="blue").grid(row = 4, column=0, padx=(0,450))
        tk.Label(self.root, text="• Lower rate limit",font = ('Arial',12)).grid(row = 5, column=0, padx=(0,440))
        tk.Label(self.root, text="• Upper rate limit",font = ('Arial',12)).grid(row = 6, column=0, padx=(0,440))
        tk.Label(self.root, text="• Ventricular amplitude",font = ('Arial',12)).grid(row = 7, column=0, padx=(0,400))
        tk.Label(self.root, text="• Ventricular pulse width",font = ('Arial',12)).grid(row = 8, column=0, padx=(0,390))

        tk.Label(self.root, text="Device:",font = ('Arial',10)).grid(row = 30, column=0, padx=(0,550),pady=(140,0))
        tk.Label(self.root, text="[Show status + Device ID]",font = ('Arial',9)).grid(row = 31, column=0, padx=(0,450),pady=(0,0))
        



    def run(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()
    


class AAI:
    def __init__(self):
        self.root = tk.Tk()
        

        self.root.title("AAI Mode")
        self.root.geometry("600x400")
        tk.Label(self.root, text="Mode: AAI", font = ('Arial',20)).grid(row = 1, column=0, padx=(70,0))
        tk.Label(self.root, text="Atrium Paced | Atrium chamber sensed | Inhibited response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(70,0), pady=(0,10))
        
        canvas = tk.Canvas(self.root,width=490, height=20)
        canvas.grid(row =0,column =0, padx=(100,0))

        #device communication status indicator
        canvas.create_oval((470,3,490,20) ,fill="blue")
        #new device approaching status indicator
        canvas.create_oval((440,3,460,20) ,fill="red")

        tk.Label(self.root, text="Parameters", font = ('Arial',15),fg="blue").grid(row = 3, column=0, padx =(0,450))
        tk.Label(self.root, text="• Lower rate limit",font = ('Arial',12)).grid(row = 4, column=0, padx=(0,440))
        tk.Label(self.root, text="• Upper rate limit",font = ('Arial',12)).grid(row = 5, column=0, padx=(0,440))
        tk.Label(self.root, text="• Atrial amplitude",font = ('Arial',12)).grid(row = 6, column=0, padx=(0,438))
        tk.Label(self.root, text="• Atrial pulse width",font = ('Arial',12)).grid(row = 7, column=0, padx=(0,430))
        tk.Label(self.root, text="• Atrial sensitivity",font = ('Arial',12)).grid(row = 8, column=0, padx=(0,440))
        tk.Label(self.root, text="• ARP",font = ('Arial',12)).grid(row = 9, column=0, padx=(0,515))
        tk.Label(self.root, text="• PVARP",font = ('Arial',12)).grid(row = 10, column=0, padx=(0,495))
        tk.Label(self.root, text="• Hystersis",font = ('Arial',12)).grid(row = 11, column=0, padx=(0,485))
        tk.Label(self.root, text="• Rate Smoothing",font = ('Arial',12)).grid(row = 12, column=0, padx=(0,440))

        tk.Label(self.root, text="Device:",font = ('Arial',10)).grid(row = 30, column=0, padx=(0,550),pady=(20,0))
        tk.Label(self.root, text="[Show status + Device ID]",font = ('Arial',9)).grid(row = 31, column=0, padx=(0,450),pady=(0,0))
        
    def run(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()

class VVI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VVI Mode")
        self.root.geometry("600x400")
        tk.Label(self.root, text="Mode: VVI", font = ('Arial',20)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self.root, text="Ventricle Paced | Ventricle chambers sensed | Inhibited response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(0,0),pady=(0,10))

        canvas = tk.Canvas(self.root,width=490, height=20)
        canvas.grid(row =0,column =0, padx=(95,0))

        #device communication status indicator
        canvas.create_oval((470,3,490,20) ,fill="blue")
        #new device approaching status indicator
        canvas.create_oval((440,3,460,20) ,fill="red")
        
        tk.Label(self.root, text="Parameters", font = ('Arial',15),fg="blue").grid(row = 3, column=0, padx=(0,450))
        tk.Label(self.root, text="• Lower rate limit",font = ('Arial',12)).grid(row = 4, column=0, padx=(0,450))
        tk.Label(self.root, text="• Upper rate limit",font = ('Arial',12)).grid(row = 5, column=0, padx=(0,450))
        tk.Label(self.root, text="• Ventricular amplitude",font = ('Arial',12)).grid(row = 6, column=0, padx=(0,410))
        tk.Label(self.root, text="• Ventrivular pulse width",font = ('Arial',12)).grid(row = 7, column=0, padx=(0,400))
        tk.Label(self.root, text="• Ventricular sensitivity",font = ('Arial',12)).grid(row = 8, column=0, padx=(0,410))
        tk.Label(self.root, text="• VRP",font = ('Arial',12)).grid(row = 9, column=0,padx=(0,521))
        tk.Label(self.root, text="• Hystersis",font = ('Arial',12)).grid(row = 10, column=0, padx=(0,491))
        tk.Label(self.root, text="• Rate Smoothing",font = ('Arial',12)).grid(row = 11, column=0, padx=(0,441))

        tk.Label(self.root, text="Device:",font = ('Arial',10)).grid(row = 30, column=0, padx=(0,550),pady=(35,0))
        tk.Label(self.root, text="[Show status + Device ID]",font = ('Arial',9)).grid(row = 31, column=0, padx=(0,450),pady=(0,0))


    def run(self):
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()
        
if __name__ == "__main__":
    aoo_app =VVI()
    #VOO done
    aoo_app.run()
        

