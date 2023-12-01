import tkinter as tk
from database.PacemakerDatabase import *
from account.LoginPage import *
import SerialCommunication


db = PacemakerDatabase.get_instance()
class ParameterProcess:
    def process_parameter(parameters,param_mode:str):
        for parameter_name,value_var in parameters:
            # Retrieve the input value for the specified parameter
            value = value_var.get()
            # Process the value (replace this with your processing logic)
            print(f"Processing {parameter_name}: {value}")
            # Serial communication goes here.
            # Write to pacemaker the parameters
            print(getUser(), param_mode, parameter_name, value)
            db.upsert_parameter_value(username = getUser(), mode= param_mode, parameter=parameter_name,value=value)

    def increment_counter(value_var1,max_val,param,param_increment):
        current_value1 = value_var1.get()
        print("current value:", current_value1)
        #print("max_val:",max_val)
        print(param)
        if((param == "Lower Rate Limit") and (50<=current_value1<90)):
            increment_val = 1
        else:
            increment_val = param_increment

        if current_value1 < max_val:
            new_value_increment =  round(current_value1 + increment_val,1) # query from database
            #print("incrementing",new_value_increment)
        else:
            messagebox.showinfo('Inavlid', 'Trying to go outside of range')
            new_value_increment =  round(current_value1,1)
            print("decrementing:",new_value_increment)
        value_var1.set(new_value_increment)

    def decrement_counter(value_var2,min_val,param2,param_increment2):
        current_value2 = value_var2.get()
        if((param2 == "Lower Rate Limit") and (50<=current_value2<90)):
            increment_val = 1
        else:
            increment_val = param_increment2

        if current_value2>min_val:
            new_value_decrement =  round(current_value2 - increment_val,1)
        else:
            messagebox.showinfo('Inavlid', 'Trying to go outside of range')
            new_value_decrement = round(current_value2,1)
        value_var2.set(new_value_decrement)
    
    def save_parameters(param_tup,mode):
        # Save all processed parameters
        parameters_to_save = [(param_name, value_var) for param_name, value_var in param_tup]
        ParameterProcess.process_parameter(parameters_to_save, mode)
        print("Parameters saved.")

    

class AOO(ParameterProcess,tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        tk.Label(self, text="Mode: AOO", font = ('Arial',23)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Atrium Paced | No chamber sensed | No response to sensing ", 
                 font = ('Arial',12)).grid(row=2,column=0,padx=(50,0),pady=(0,10))
        
        """Check if the user has any saved parameters
       If so, use those values as the default values
       Otherwise, use the default values from the modeparam table"""

        parameters = db.get_parameters(mode = "AOO")  # 4 parameters assigned to mode AOO
        print(getUser())
        saved_value = db.get_parameters(username = getUser(), mode = "AOO")  # length 4 means theres 4 saved parameters for this user for AOO
        print(saved_value)
        # print(parameters)
        # SETS AND SAVES VALUES TO TEXT FIELDS
        
        self.parameter_tuples: list(tuple) = []
        parameters_max = []
        parameters_min = []
        parameters_increment =[]
        i=0
        row = 5
        for param in parameters:
            
            #parameters= db.get_modes_from_modeparameters()
            #print(parameters[i])
            default_val = parameters[i][3]
            
            #print("param max",parameter_max)
            
            value = tk.DoubleVar()
            print("Check if saved value length matches parameter value length", len(saved_value), len(parameters))
            if len(saved_value) == len(parameters):
                value.set(saved_value[i][3])
                self.parameter_tuples.append((saved_value[i][2], value))
                #print("saved value:", value)
            else: 
                value.set(default_val)
                self.parameter_tuples.append((param[1], value))

            # print(param[1])
            
            #self.parameter_tuples.append((saved_value[i][2], value))
            print(self.parameter_tuples[i][0], self.parameter_tuples[i][1].get())

            label = tk.Label(self, text=f" {param[1]}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(10, 10))
    
            parameters_increment.append(parameters[i][6])

            parameters_max.append(parameters[i][5])
            self.increment_button = tk.Button(self, text="+", command=lambda v=value, i=i, mode="AOO": ParameterProcess.increment_counter(v, parameters_max[i], self.parameter_tuples[i][0], parameters_increment[i]))
            self.increment_button.grid(row=row, column=0, padx=(200, 100)) 

            value_str=tk.StringVar()
            value_str.set(value.get())

            num = tk.Label(self, textvariable=value_str, font=('Arial', 17))
            num.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label

        
            parameters_min.append(parameters[i][4])
            self.decrement_button = tk.Button(self, text="-", command=lambda v=value, i=i, mode="AOO", j=i: ParameterProcess.decrement_counter(v, parameters_min[i], mode, parameters_increment[j]))
            self.decrement_button.grid(row=row, column=0, padx=(0, 200)) 
            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param[1], v=value,m="AOO": ParameterProcess.process_parameter([(p,v)],m))
            
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            #print("self parameter tuplesss", self.parameter_tuples)
            #print("saved valyh", saved_value)

            SerialCommunication.set_parameters(MODE =1, LRL=saved_value[3][3],URL = saved_value[2][3],ATR_AMP= saved_value[0][3],ATR_PW=saved_value[1][3])
            row += 1
            i+=1
        
        save_button = tk.Button(self, text="Save", command=lambda pt=self.parameter_tuples, mode="AOO": ParameterProcess.save_parameters(pt, mode))
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))
        SerialCommunication.set_parameters(MODE =1, LRL=saved_value[3][3],URL = saved_value[2][3],ATR_AMP= saved_value[0][3],ATR_PW=saved_value[1][3])

        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()

class VOO(ParameterProcess,tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self, text="MODE: VOO", font = ('Arial',20)).grid(row = 1, column=0, padx=(70,0))
        tk.Label(self, text="Ventrical Paced | No chamber sensed | No response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(70,0),pady=(0,10))
        
        parameters = db.get_parameters(mode = "VOO")  # 4 parameters assigned to mode AOO
        print(getUser())
        saved_value = db.get_parameters(username = getUser(), mode = "VOO")  # length 4 means theres 4 saved parameters for this user for AOO
        print(saved_value)
        # print(parameters)
        # SETS AND SAVES VALUES TO TEXT FIELDS
        
        self.parameter_tuples: list(tuple) = []
        parameters_max = []
        parameters_min = []
        parameters_increment =[]
        i=0
        row = 5
        for param in parameters:
            
            #parameters= db.get_modes_from_modeparameters()
            #print(parameters[i])
            default_val = parameters[i][3]
            
            #print("param max",parameter_max)
            
            value = tk.DoubleVar()
            print("Check if saved value length matches parameter value length", len(saved_value), len(parameters))
            if len(saved_value) == len(parameters):
                value.set(saved_value[i][3])
                self.parameter_tuples.append((saved_value[i][2], value))
                #print("saved value:", value)
            else: 
                value.set(default_val)
                self.parameter_tuples.append((param[1], value))

            # print(param[1])
            
            #self.parameter_tuples.append((saved_value[i][2], value))
            print(self.parameter_tuples[i][0], self.parameter_tuples[i][1].get())

            label = tk.Label(self, text=f" {param[1]}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(10, 10))
    
            parameters_increment.append(parameters[i][6])

            parameters_max.append(parameters[i][5])
            self.increment_button = tk.Button(self, text="+", command=lambda v=value, i=i, mode="VOO": ParameterProcess.increment_counter(v, parameters_max[i], self.parameter_tuples[i][0], parameters_increment[i]))
            self.increment_button.grid(row=row, column=0, padx=(200, 100)) 
        

            value_str=tk.StringVar()
            value_str.set(value.get())

            num = tk.Label(self, textvariable=value_str, font=('Arial', 17))
            num.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label

        
            parameters_min.append(parameters[i][4])
            self.decrement_button = tk.Button(self, text="-", command=lambda v=value, i=i, mode="VOO", j=i: ParameterProcess.decrement_counter(v, parameters_min[i], mode, parameters_increment[j]))
            self.decrement_button.grid(row=row, column=0, padx=(0, 200)) 
            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param[1], v=value,m="VOO": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
            i+=1
        
        save_button = tk.Button(self, text="Save", command=lambda pt=self.parameter_tuples, mode="VOO": ParameterProcess.save_parameters(pt, mode))
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))

        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()


class AAI (ParameterProcess,tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self, text="Mode: AAI", font = ('Arial',20)).grid(row = 1, column=0, padx=(70,0))
        tk.Label(self, text="Atrium Paced | Atrium chamber sensed | Inhibited response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(70,0), pady=(0,10))
        
        parameters = db.get_parameters(mode = "AAI")  # 4 parameters assigned to mode AOO
        print(getUser())
        saved_value = db.get_parameters(username = getUser(), mode = "AAI")  # length 4 means theres 4 saved parameters for this user for AOO
        print(saved_value)
        # print(parameters)
        # SETS AND SAVES VALUES TO TEXT FIELDS
        
        self.parameter_tuples: list(tuple) = []
        parameters_max = []
        parameters_min = []
        parameters_increment =[]
        i=0
        row = 5
        for param in parameters:
            
            #parameters= db.get_modes_from_modeparameters()
            #print(parameters[i])
            default_val = parameters[i][3]
            
            #print("param max",parameter_max)
            
            value = tk.DoubleVar()
            print("Check if saved value length matches parameter value length", len(saved_value), len(parameters))
            if len(saved_value) == len(parameters):
                value.set(saved_value[i][3])
                self.parameter_tuples.append((saved_value[i][2], value))
                #print("saved value:", value)
            else: 
                value.set(default_val)
                self.parameter_tuples.append((param[1], value))

            # print(param[1])
            
            #self.parameter_tuples.append((saved_value[i][2], value))
            print(self.parameter_tuples[i][0], self.parameter_tuples[i][1].get())

            label = tk.Label(self, text=f" {param[1]}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(10, 10))
    
            parameters_increment.append(parameters[i][6])

            parameters_max.append(parameters[i][5])
            self.increment_button = tk.Button(self, text="+", command=lambda v=value, i=i, mode="AAI": ParameterProcess.increment_counter(v, parameters_max[i], self.parameter_tuples[i][0], parameters_increment[i]))
            self.increment_button.grid(row=row, column=0, padx=(200, 100)) 

            value_str=tk.StringVar()
            value_str.set(value.get())

            num = tk.Label(self, textvariable=value_str, font=('Arial', 17))
            num.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label

        
            parameters_min.append(parameters[i][4])
            self.decrement_button = tk.Button(self, text="-", command=lambda v=value, i=i, mode="AAI", j=i: ParameterProcess.decrement_counter(v, parameters_min[i], mode, parameters_increment[j]))
            self.decrement_button.grid(row=row, column=0, padx=(0, 200)) 
            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param[1], v=value,m="AAI": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
            i+=1
        
        save_button = tk.Button(self, text="Save", command=lambda pt=self.parameter_tuples, mode="AAI": ParameterProcess.save_parameters(pt, mode))
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))

        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()

class VVI(ParameterProcess,tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self, text="Mode: VVI", font = ('Arial',20)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Ventricle Paced | Ventricle chambers sensed | Inhibited response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(0,0),pady=(0,10))

        parameters = db.get_parameters(mode = "VVI")  # 4 parameters assigned to mode AOO
        print(getUser())
        saved_value = db.get_parameters(username = getUser(), mode = "VVI")  # length 4 means theres 4 saved parameters for this user for AOO
        print(saved_value)
        # print(parameters)
        # SETS AND SAVES VALUES TO TEXT FIELDS
        
        self.parameter_tuples: list(tuple) = []
        parameters_max = []
        parameters_min = []
        parameters_increment =[]
        i=0
        row = 5
        for param in parameters:
            
            #parameters= db.get_modes_from_modeparameters()
            #print(parameters[i])
            default_val = parameters[i][3]
            
            #print("param max",parameter_max)
            
            value = tk.DoubleVar()
            print("Check if saved value length matches parameter value length", len(saved_value), len(parameters))
            if len(saved_value) == len(parameters):
                value.set(saved_value[i][3])
                self.parameter_tuples.append((saved_value[i][2], value))
                #print("saved value:", value)
            else: 
                value.set(default_val)
                self.parameter_tuples.append((param[1], value))

            # print(param[1])
            
            #self.parameter_tuples.append((saved_value[i][2], value))
            print(self.parameter_tuples[i][0], self.parameter_tuples[i][1].get())

            label = tk.Label(self, text=f" {param[1]}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(10, 10))
    
            parameters_increment.append(parameters[i][6])

            parameters_max.append(parameters[i][5])
            self.increment_button = tk.Button(self, text="+", command=lambda v=value, i=i, mode="VVI": ParameterProcess.increment_counter(v, parameters_max[i], self.parameter_tuples[i][0], parameters_increment[i]))
            self.increment_button.grid(row=row, column=0, padx=(200, 100)) 

            value_str=tk.StringVar()
            value_str.set(value.get())

            num = tk.Label(self, textvariable=value_str, font=('Arial', 17))
            num.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label

        
            parameters_min.append(parameters[i][4])
            self.decrement_button = tk.Button(self, text="-", command=lambda v=value, i=i, mode="VVI", j=i: ParameterProcess.decrement_counter(v, parameters_min[i], mode, parameters_increment[j]))
            self.decrement_button.grid(row=row, column=0, padx=(0, 200)) 
            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param[1], v=value,m="VVI": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
            i+=1
        
        save_button = tk.Button(self, text="Save", command=lambda pt=self.parameter_tuples, mode="VVI": ParameterProcess.save_parameters(pt, mode))
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))

        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()

class AOOR(ParameterProcess,tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        tk.Label(self, text="Mode: AOOR", font = ('Arial',23)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Atrium Paced | No chamber sensed | No response to sensing ", 
                 font = ('Arial',12)).grid(row=2,column=0,padx=(50,0),pady=(0,10))
        
        """Check if the user has any saved parameters
       If so, use those values as the default values
       Otherwise, use the default values from the modeparam table"""

        parameters = db.get_parameters(mode = "AOOR")  # 4 parameters assigned to mode AOO
        print(getUser())
        saved_value = db.get_parameters(username = getUser(), mode = "AOOR")  # length 4 means theres 4 saved parameters for this user for AOO
        print(saved_value)
        # print(parameters)
        # SETS AND SAVES VALUES TO TEXT FIELDS
        
        self.parameter_tuples: list(tuple) = []
        parameters_max = []
        parameters_min = []
        parameters_increment =[]
        i=0
        row = 5
        for param in parameters:
            
            #parameters= db.get_modes_from_modeparameters()
            #print(parameters[i])
            default_val = parameters[i][3]
            
            #print("param max",parameter_max)
            
            value = tk.DoubleVar()
            print("Check if saved value length matches parameter value length", len(saved_value), len(parameters))
            if len(saved_value) == len(parameters):
                value.set(saved_value[i][3])
                self.parameter_tuples.append((saved_value[i][2], value))
                #print("saved value:", value)
            else: 
                value.set(default_val)
                self.parameter_tuples.append((param[1], value))

            # print(param[1])
            
            #self.parameter_tuples.append((saved_value[i][2], value))
            print(self.parameter_tuples[i][0], self.parameter_tuples[i][1].get())

            label = tk.Label(self, text=f" {param[1]}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(10, 10))
    
            parameters_increment.append(parameters[i][6])

            parameters_max.append(parameters[i][5])
            self.increment_button = tk.Button(self, text="+", command=lambda v=value, i=i, mode="AOOR": ParameterProcess.increment_counter(v, parameters_max[i], self.parameter_tuples[i][0], parameters_increment[i]))
            self.increment_button.grid(row=row, column=0, padx=(200, 100)) 

            value_str=tk.StringVar()
            value_str.set(value.get())

            num = tk.Label(self, textvariable=value_str, font=('Arial', 17))
            num.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label

        
            parameters_min.append(parameters[i][4])
            self.decrement_button = tk.Button(self, text="-", command=lambda v=value, i=i, mode="AOOR", j=i: ParameterProcess.decrement_counter(v, parameters_min[i], mode, parameters_increment[j]))
            self.decrement_button.grid(row=row, column=0, padx=(0, 200)) 
            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param[1], v=value,m="AOOR": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
            i+=1
        
        save_button = tk.Button(self, text="Save", command=lambda pt=self.parameter_tuples, mode="AOOR": ParameterProcess.save_parameters(pt, mode))
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))

        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()

class VOOR(ParameterProcess,tk.Frame):

    def __init__(self,parent):
        super().__init__(parent)
        
        tk.Label(self, text="Mode: VOOR", font = ('Arial',23)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Atrium Paced | No chamber sensed | No response to sensing ", 
                 font = ('Arial',12)).grid(row=2,column=0,padx=(50,0),pady=(0,10))
        
        """Check if the user has any saved parameters
       If so, use those values as the default values
       Otherwise, use the default values from the modeparam table"""

        parameters = db.get_parameters(mode = "VOOR")  # 4 parameters assigned to mode AOO
        print(getUser())
        saved_value = db.get_parameters(username = getUser(), mode = "VOOR")  # length 4 means theres 4 saved parameters for this user for AOO
        print(saved_value)
        # print(parameters)
        # SETS AND SAVES VALUES TO TEXT FIELDS
        
        self.parameter_tuples: list(tuple) = []
        parameters_max = []
        parameters_min = []
        parameters_increment =[]
        i=0
        row = 5
        for param in parameters:
            
            #parameters= db.get_modes_from_modeparameters()
            #print(parameters[i])
            default_val = parameters[i][3]
            
            #print("param max",parameter_max)
            
            value = tk.DoubleVar()
            print("Check if saved value length matches parameter value length", len(saved_value), len(parameters))
            if len(saved_value) == len(parameters):
                value.set(saved_value[i][3])
                self.parameter_tuples.append((saved_value[i][2], value))
                #print("saved value:", value)
            else: 
                value.set(default_val)
                self.parameter_tuples.append((param[1], value))

            # print(param[1])
            
            #self.parameter_tuples.append((saved_value[i][2], value))
            print(self.parameter_tuples[i][0], self.parameter_tuples[i][1].get())

            label = tk.Label(self, text=f" {param[1]}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(10, 10))
    
            parameters_increment.append(parameters[i][6])

            parameters_max.append(parameters[i][5])
            self.increment_button = tk.Button(self, text="+", command=lambda v=value, i=i, mode="VOOR": ParameterProcess.increment_counter(v, parameters_max[i], self.parameter_tuples[i][0], parameters_increment[i]))
            self.increment_button.grid(row=row, column=0, padx=(200, 100)) 

            value_str=tk.StringVar()
            value_str.set(value.get())

            num = tk.Label(self, textvariable=value_str, font=('Arial', 17))
            num.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label

        
            parameters_min.append(parameters[i][4])
            self.decrement_button = tk.Button(self, text="-", command=lambda v=value, i=i, mode="VOOR", j=i: ParameterProcess.decrement_counter(v, parameters_min[i], mode, parameters_increment[j]))
            self.decrement_button.grid(row=row, column=0, padx=(0, 200)) 
            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param[1], v=value,m="VOOR": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
            i+=1
        
        save_button = tk.Button(self, text="Save", command=lambda pt=self.parameter_tuples, mode="VOOR": ParameterProcess.save_parameters(pt, mode))
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))

        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()

class AAIR(ParameterProcess,tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        tk.Label(self, text="Mode: AAIR", font = ('Arial',23)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Atrium Paced | No chamber sensed | No response to sensing ", 
                 font = ('Arial',12)).grid(row=2,column=0,padx=(50,0),pady=(0,10))
        
        """Check if the user has any saved parameters
       If so, use those values as the default values
       Otherwise, use the default values from the modeparam table"""

        parameters = db.get_parameters(mode = "AAIR")  # 4 parameters assigned to mode AOO
        print(getUser())
        saved_value = db.get_parameters(username = getUser(), mode = "AAIR")  # length 4 means theres 4 saved parameters for this user for AOO
        print(saved_value)
        # print(parameters)
        # SETS AND SAVES VALUES TO TEXT FIELDS
        
        self.parameter_tuples: list(tuple) = []
        parameters_max = []
        parameters_min = []
        parameters_increment =[]
        i=0
        row = 5
        for param in parameters:
            
            #parameters= db.get_modes_from_modeparameters()
            #print(parameters[i])
            default_val = parameters[i][3]
            
            #print("param max",parameter_max)
            
            value = tk.DoubleVar()
            print("Check if saved value length matches parameter value length", len(saved_value), len(parameters))
            if len(saved_value) == len(parameters):
                value.set(saved_value[i][3])
                self.parameter_tuples.append((saved_value[i][2], value))
                #print("saved value:", value)
            else: 
                value.set(default_val)
                self.parameter_tuples.append((param[1], value))

            # print(param[1])
            
            #self.parameter_tuples.append((saved_value[i][2], value))
            print(self.parameter_tuples[i][0], self.parameter_tuples[i][1].get())

            label = tk.Label(self, text=f" {param[1]}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(10, 10))
    
            parameters_increment.append(parameters[i][6])

            parameters_max.append(parameters[i][5])
            self.increment_button = tk.Button(self, text="+", command=lambda v=value, i=i, mode="AAIR": ParameterProcess.increment_counter(v, parameters_max[i], self.parameter_tuples[i][0], parameters_increment[i]))
            self.increment_button.grid(row=row, column=0, padx=(200, 100)) 

            value_str=tk.StringVar()
            value_str.set(value.get())

            num = tk.Label(self, textvariable=value_str, font=('Arial', 17))
            num.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label

        
            parameters_min.append(parameters[i][4])
            self.decrement_button = tk.Button(self, text="-", command=lambda v=value, i=i, mode="AAIR", j=i: ParameterProcess.decrement_counter(v, parameters_min[i], mode, parameters_increment[j]))
            self.decrement_button.grid(row=row, column=0, padx=(0, 200)) 
            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param[1], v=value,m="AAIR": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
            i+=1
        
        save_button = tk.Button(self, text="Save", command=lambda pt=self.parameter_tuples, mode="AAIR": ParameterProcess.save_parameters(pt, mode))
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))

        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()      

class VVIR(ParameterProcess,tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        tk.Label(self, text="Mode: VVIR", font = ('Arial',23)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Atrium Paced | No chamber sensed | No response to sensing ", 
                 font = ('Arial',12)).grid(row=2,column=0,padx=(50,0),pady=(0,10))
        
        """Check if the user has any saved parameters
       If so, use those values as the default values
       Otherwise, use the default values from the modeparam table"""

        parameters = db.get_parameters(mode = "VVIR")  # 4 parameters assigned to mode AOO
        print(getUser())
        saved_value = db.get_parameters(username = getUser(), mode = "VVIR")  # length 4 means theres 4 saved parameters for this user for AOO
        print(saved_value)
        # print(parameters)
        # SETS AND SAVES VALUES TO TEXT FIELDS
        
        self.parameter_tuples: list(tuple) = []
        parameters_max = []
        parameters_min = []
        parameters_increment =[]
        i=0
        row = 5
        for param in parameters:
            
            #parameters= db.get_modes_from_modeparameters()
            #print(parameters[i])
            default_val = parameters[i][3]
            
            #print("param max",parameter_max)
            
            value = tk.DoubleVar()
            print("Check if saved value length matches parameter value length", len(saved_value), len(parameters))
            if len(saved_value) == len(parameters):
                value.set(saved_value[i][3])
                self.parameter_tuples.append((saved_value[i][2], value))
                #print("saved value:", value)
            else: 
                value.set(default_val)
                self.parameter_tuples.append((param[1], value))

            # print(param[1])
            
            #self.parameter_tuples.append((saved_value[i][2], value))
            print(self.parameter_tuples[i][0], self.parameter_tuples[i][1].get())

            label = tk.Label(self, text=f" {param[1]}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(10, 10))
    
            parameters_increment.append(parameters[i][6])

            parameters_max.append(parameters[i][5])
            self.increment_button = tk.Button(self, text="+", command=lambda v=value, i=i, mode="VVIR": ParameterProcess.increment_counter(v, parameters_max[i], self.parameter_tuples[i][0], parameters_increment[i]))
            self.increment_button.grid(row=row, column=0, padx=(200, 100)) 

            value_str=tk.StringVar()
            value_str.set(value.get())

            num = tk.Label(self, textvariable=value_str, font=('Arial', 17))
            num.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label

        
            parameters_min.append(parameters[i][4])
            self.decrement_button = tk.Button(self, text="-", command=lambda v=value, i=i, mode="VVIR", j=i: ParameterProcess.decrement_counter(v, parameters_min[i], mode, parameters_increment[j]))
            self.decrement_button.grid(row=row, column=0, padx=(0, 200)) 
            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param[1], v=value,m="VVIR": ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
            i+=1
        
        save_button = tk.Button(self, text="Save", command=lambda pt=self.parameter_tuples, mode="VVIR": ParameterProcess.save_parameters(pt, mode))
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))

        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()
