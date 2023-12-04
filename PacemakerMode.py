import tkinter as tk
from database.PacemakerDatabase import *
from account.LoginPage import *
import SerialCommunication as sc

db = PacemakerDatabase.get_instance()
class ParameterProcess:
    def process_parameter(parameters,param_mode:str):
        for parameter_name, value_var in parameters:
            value = value_var.get()
            # Serial communication goes here.
            # Write to pacemaker the parameters
            db.upsert_parameter_value(username = getUser(), mode = param_mode, parameter = parameter_name, value = value)

    def increment_counter(self,value_var1,max_val,param,param_increment):
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

    def decrement_counter(self,value_var2,min_val,param2,param_increment2):
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
    
    def save_parameters(self, param_tuple, mode: str):
        # Save all processed parameters
        parameters_to_save = [(param_name, value_var) for param_name, value_var in param_tuple]
        print(parameters_to_save)
        ParameterProcess.process_parameter(parameters_to_save, mode)
        print("Parameters saved.")

class Mode():
    def __init__(self, mode, subtitle, parameters):
        self.mode = mode
        self.subtitle = subtitle
        self.parameters = parameters

    def get_mode(self):
        return self.mode
    
    def get_subtitle(self):
        return self.subtitle
    
    def get_parameters(self):
        return self.parameters

class ProcessMode(tk.Frame, ParameterProcess):
    def __init__(self, parent: tk.Frame, mode: Mode):
        super().__init__(parent)
        self.mode: str = mode.get_mode()
        self.subtitle: str = mode.get_subtitle()
        self.parameters: list = mode.get_parameters()
        self.set_display()

    def set_display(self):
        """Sets the display for the mode page."""

        # Set the title and subtitle
        tk.Label(self, text=f"Mode: {self.mode}", font=('Arial', 23)).grid(row=1, column=0, padx=(50, 0))
        tk.Label(self, text=self.subtitle, font=('Arial', 12)).grid(row=2, column=0, padx=(50, 0), pady=(0, 10))

        # Check if the user has any saved parameters
        account_parameters = db.get_parameters(username = getUser(), mode = self.mode)
        mode_parameters = db.get_parameters(mode = self.mode)
        
        self.parameter_tuples: list(tuple) = []        
        parameters_max = []
        parameters_min = []
        parameters_increment =[]
        i = 0; row = 5

        # Set up buttons and labels for each parameter
        for param in mode_parameters:
            default_val = param[3]
            value = tk.DoubleVar(self)
            if len(account_parameters) == len(mode_parameters) and len(account_parameters) != 0:
                data = db.get_parameters(username = getUser(), mode = self.mode, parameter = param[1])[0]
                parameter_name = data[2]
                parameter_value = data[3]
                value.set(parameter_value)
                self.parameter_tuples.append((parameter_name, value)) 
            else: 
                value.set(default_val)
                parameter_name = param[1]
                self.parameter_tuples.append((parameter_name, value))

            # Parameter label
            label = tk.Label(self, text=f" {param[1]}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))

            # Increment variables
            parameters_increment.append(mode_parameters[i][6])
            parameters_max.append(mode_parameters[i][5])

            # Decrement button
            parameters_min.append(param[4])
            decrement_button = tk.Button(self, text="-", command = lambda v = value, i = i,mode=self.mode,j=i: \
                                         self.decrement_counter(v, parameters_min[i],mode,parameters_increment[j]))
            decrement_button.grid(row=row, column=0, padx=(0, 100))

            # Increment button
            increment_button = tk.Button(self, text="+", command = lambda v =value, i = i: self.increment_counter(v, parameters_max[i],self.parameter_tuples[i][0],parameters_increment[i]))
            increment_button.grid(row=row, column=0, padx=(100, 0))

            # Parameter value
            parameter_value = tk.Label(self, textvariable=value, font=('Arial', 16))
            parameter_value.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label
            
            # Process button
            process_button = tk.Button(self, text=f"Process", command=lambda p=param[1], v=value,m=self.mode: ParameterProcess.process_parameter([(p,v)],m))
            process_button.grid(row=row, column=0,padx=(300, 50))

            row+=1; i+=1

        # Save button
        save_button = tk.Button(self, text="Save", command = lambda p=self.parameter_tuples, m=self.mode: self.save_parameters(p, m))
        save_button.grid(row=row, column=0, padx=(300, 50), pady=(20, 0))

        # Device label
        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()

    def get_mode(self):
        return self.mode
    
    def get_subtitle(self):
        return self.subtitle
    
    def get_parameters(self):
        return db.get_parameters(mode = self.mode)
    
    def format_parameter_tuples(self):
        accountparameters = db.load_param_value_pairs()
        modeparameters = db.get_parameters(mode = self.mode)
        if len(accountparameters) != len(modeparameters):
            for param in modeparameters:
                if param[1] not in accountparameters:
                    accountparameters[param[1]] = param[3]
    

class AOO(Mode):
    def __init__(self):
        Mode.__init__(self, mode="AOO", 
                        subtitle="Atrium Paced | No chamber sensed | No response to sensing ", 
                        parameters=db.get_parameters(mode = "AOO"))
    
    def format_serial_communication(self):
        """Formats the serial communication for the AOO mode."""
        # sc.set_parameters(mode = 1, LRL = )
        
class VOO(Mode):
    def __init__(self):
        Mode.__init__(self, mode="VOO", 
                        subtitle="Ventricle Paced | No chamber sensed | No response to sensing ", 
                        parameters=db.get_parameters(mode = "VOO"))
        
class AAI(Mode):
    def __init__(self):
        Mode.__init__(self, mode="AAI", 
                        subtitle="Atrium Paced | Atrium Sensed | Inhibited response to sensing ", 
                        parameters=db.get_parameters(mode = "AAI"))

class VVI(Mode):
    def __init__(self):
        Mode.__init__(self, mode="VVI", 
                        subtitle="Ventricle Paced | Ventricle Sensed | Inhibited response to sensing ", 
                        parameters=db.get_parameters(mode = "VVI"))

class AOOR(Mode):
    def __init__(self):
        Mode.__init__(self, mode="AOOR", 
                        subtitle="Atrium Paced | No chamber sensed | Rate response to activity ", 
                        parameters=db.get_parameters(mode = "AOOR"))

class VOOR(Mode):
    def __init__(self):
        Mode.__init__(self, mode="VOOR", 
                        subtitle="Ventricle Paced | No chamber sensed | Rate response to activity ", 
                        parameters=db.get_parameters(mode = "VOOR"))

class AAIR(Mode):
    def __init__(self):
        Mode.__init__(self, mode="AAIR", 
                        subtitle="Atrium Paced | Atrium Sensed | Rate response to activity ", 
                        parameters=db.get_parameters(mode = "AAIR"))
        
class VVIR(Mode):
    def __init__(self):
        Mode.__init__(self, mode="VVIR", 
                        subtitle="Ventricle Paced | Ventricle Sensed | Rate response to activity ", 
                        parameters=db.get_parameters(mode = "VVIR"))