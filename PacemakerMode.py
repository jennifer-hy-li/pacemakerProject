import tkinter as tk
from database.PacemakerDatabase import *
from account.LoginPage import *

db = PacemakerDatabase.get_instance()
class ParameterProcess:
    def process_parameter(parameters,param_mode:str):
        for parameter_name,value_var in parameters:
            # Retrieve the input value for the specified parameter
            value = value_var.get()
            # Process the value (replace this with your processing logic)
            print(f"Processing {parameter_name}: {value}")
            db.upsert_parameter_value(username = getUser(), mode= param_mode, parameter=parameter_name,value=value)

    def increment_counter(self,value_var1,max_val):
        current_value1 = value_var1.get()
        print("current value:", current_value1)
        print("max_val:",max_val)
        if current_value1 < max_val:
            new_value_increment =  round(current_value1 + 0.1,1)
            print("incrementing",new_value_increment)
        else:
            new_value_increment =  round(current_value1,1)
            print("decrementing:",new_value_increment)
        value_var1.set(new_value_increment)

    def decrement_counter(self,value_var2,min_val):
        current_value2 = value_var2.get()

        if current_value2>min_val:
            new_value_decrement =  round(current_value2 - 0.1,1)
        else:
            new_value_decrement = round(current_value2,1)
        value_var2.set(new_value_decrement)
    

class AOO(ParameterProcess,tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        tk.Label(self, text="Mode: AOO", font = ('Arial',23)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Atrium Paced | No chamber sensed | No response to sensing ", 
                 font = ('Arial',12)).grid(row=2,column=0,padx=(50,0),pady=(0,10))
        
        # Create Entry widgets for parameters
        self.param_entries = {}
        self.parameter_values = {}

        parameters = db.get_parameters(mode ="AOO")
        parameter_tuples: list(tuple) = []
        i=0
        
        modeparam_table= db.get_modes_from_modeparameters()
        print(parameters)
        for param in parameters:
            
            #modeparam_table= db.get_modes_from_modeparameters()
            parameter_max =modeparam_table[i][5]
            parameter_min = modeparam_table[i][4]
            default_val = modeparam_table[i][3]
            
            #print("param max",parameter_max)
            
            value = tk.DoubleVar()
            saved_value = db.get_all_account_parameters(getUser())
            default_val = modeparam_table[i][3]
            if saved_value is not None and len(saved_value)>0 and i<len(saved_value):
                value.set(saved_value[i][3])
                #print("saved value:", value)
            else: 
                value.set(default_val)
            i+=1
            print(param[1])
            parameter_tuples.append((param[1], value))
        

        row = 5  # Starting row for parameters
        for parameter_name, value_var in parameter_tuples:
            label = tk.Label(self, text=f" {parameter_name}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))
    
            
            self.increment_button = tk.Button(self, text="+", command= lambda v =value_var: self.increment_counter(v,parameter_max))
            self.increment_button.grid(row=row, column=0, padx=(100, 0)) 

            num = tk.Label(self, textvariable=value_var, font=('Arial', 16))
            num.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label

            self.decrement_button = tk.Button(self, text="-", command=lambda v= value_var: self.decrement_counter(v,parameter_min))
            self.decrement_button.grid(row=row, column=0, padx=(0, 100)) 
            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=parameter_name, v=value_var,m="AOO": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
        
        save_button = tk.Button(self, text="Save", command=self.save_parameters)
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))

        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()

    def save_parameters(self):
        # Save all processed parameters
        parameters_to_save = [(param_name, value_var) for param_name, value_var in self.parameter_values.items()]
        ParameterProcess.process_parameter(parameters_to_save, "AOO")
        print("Parameters saved.")

class VOO(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self, text="MODE: VOO", font = ('Arial',20)).grid(row = 1, column=0, padx=(70,0))
        tk.Label(self, text="Ventrical Paced | No chamber sensed | No response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(70,0),pady=(0,10))
        
        # Create Entry widgets for parameters
        self.param_entries = {}
        self.parameter_values = {}

        parameters = db.get_parameters(mode ="VOO")
        parameter_tuples: list(tuple) = []
        for param in parameters:
            value = tk.StringVar()
            print(param)
            parameter_tuples.append((param[1], value))
        
        row = 5  # Starting row for parameters
        for parameter_name, value_var in parameter_tuples:
            label = tk.Label(self, text=f" {parameter_name}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))
            entry = tk.Entry(self, textvariable=value_var)
            entry.grid(row=row, column=0, padx=(50, 0))  # Use padx to adjust the spacing
            self.param_entries[parameter_name] = entry

            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=parameter_name, v=value_var,m="VOO": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
        
        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()


class AAI (tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self, text="Mode: AAI", font = ('Arial',20)).grid(row = 1, column=0, padx=(70,0))
        tk.Label(self, text="Atrium Paced | Atrium chamber sensed | Inhibited response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(70,0), pady=(0,10))
        
        # Create Entry widgets for parameters
        self.param_entries = {}
        self.parameter_values = {}

        parameters = db.get_parameters(mode ="AAI")
        parameter_tuples: list(tuple) = []
        for param in parameters:
            value = tk.StringVar()
            print(param)
            parameter_tuples.append((param[1], value))
        
        row = 5  # Starting row for parameters
        for parameter_name, value_var in parameter_tuples:
            label = tk.Label(self, text=f" {parameter_name}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))
            entry = tk.Entry(self, textvariable=value_var)
            entry.grid(row=row, column=0, padx=(50, 0))  # Use padx to adjust the spacing
            self.param_entries[parameter_name] = entry

            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=parameter_name, v=value_var,m="AAI": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0, padx=(300, 50))
            row += 1
       
        tk.Label(self, text="Device:",font = ('Arial',10)).grid(row = 30, column=0, padx=(0,550),pady=(20,0))
        tk.Label(self, text="[Show status + Device ID]",font = ('Arial',9)).grid(row = 31, column=0, padx=(0,450),pady=(0,0))
        
        self.pack()

class VVI(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self, text="Mode: VVI", font = ('Arial',20)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Ventricle Paced | Ventricle chambers sensed | Inhibited response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(0,0),pady=(0,10))

        # Create Entry widgets for parameters
        self.param_entries = {}
        self.parameter_values = {}

        parameters = db.get_parameters(mode ="VVI")
        parameter_tuples: list(tuple) = []
        for param in parameters:
            value = tk.StringVar()
            print(param)
            parameter_tuples.append((param[1], value))
        
        row = 5  # Starting row for parameters
        for parameter_name, value_var in parameter_tuples:
            label = tk.Label(self, text=f" {parameter_name}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))
            entry = tk.Entry(self, textvariable=value_var)
            entry.grid(row=row, column=0, padx=(50, 0))  # Use padx to adjust the spacing
            self.param_entries[parameter_name] = entry

            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=parameter_name, v=value_var,m="VVI": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0, padx=(300, 50))
            row += 1

        tk.Label(self, text="Device:",font = ('Arial',10)).grid(row = 30, column=0, padx=(0,550),pady=(35,0))
        tk.Label(self, text="[Show status + Device ID]",font = ('Arial',9)).grid(row = 31, column=0, padx=(0,450),pady=(0,0))

        self.pack()
