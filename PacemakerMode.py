# Authors: Angeline Segado, Jayden Hooper

import tkinter as tk
from database.PacemakerDatabase import *
from account.LoginPage import *
import serial_coms.SerialCommunication as sc

db = PacemakerDatabase.get_instance()

class Mode():
    def __init__(self, mode, subtitle):
        self.mode: str = mode
        self.subtitle: str = subtitle
        self.mode_parameters = db.get_parameters(mode = self.mode)
        self.account_parameters = db.load_param_value_pairs(username = getUser(), mode = self.mode)
        self.min_list: list = []
        self.max_list: list = []
        self.increment_list: list = []
        self.parameters: list(tuple) = self.format_parameter_tuples()
        self.serial_params: list(tuple) = self.format_serial_communication()

    def get_mode(self):
        return self.mode
    
    def get_subtitle(self):
        return self.subtitle
    
    def get_parameters(self):
        return self.parameters
    
    def format_parameter_tuples(self):
        """Formats the parameter tuples for each Mode in 
        the format (parameter name, parameter value)."""
        parameters = []
        if len(self.mode_parameters) == len(self.account_parameters) and len(self.account_parameters) != 0:
            for param in self.account_parameters:
                parameters.append(param)
                self.min_list.append([p[4] for p in self.mode_parameters if p[1] == param[0]][0])
                self.max_list.append([p[5] for p in self.mode_parameters if p[1] == param[0]][0])
                self.increment_list.append([p[6] for p in self.mode_parameters if p[1] == param[0]][0])
            return parameters
        for tuple in self.mode_parameters:
            if tuple[1] not in [p[0] for p in self.account_parameters]:
                parameters.append((tuple[1], tuple[3])) # (parameter name, default value)
            else:
                value = [p[1] for p in self.account_parameters if p[0] == tuple[1]][0]
                parameters.append((tuple[1], value))
            self.min_list.append(tuple[4])
            self.max_list.append(tuple[5])
            self.increment_list.append(tuple[6])
        return parameters

    def format_serial_communication(self):
        """Formats the serial communication for any mode."""
        map = sc.get_parameter_map()
        serial_params = []
        for param_name, param_value in self.parameters:
            if param_name in map:
                serial_params.append((map[param_name], param_value))
        return serial_params

    def send_params_serial(self):
        """Sends the parameters to the pacemaker."""
        args = {}
        for param_name, param_value in self.serial_params:
            args[param_name] = param_value
        sc.write(sc.set_parameters(RECEIVE = False, 
                                   MODE = sc.get_mode_number(self.mode),
                                      **args))

class ParameterProcess:
    """Class to process the parameters."""

    @staticmethod
    def process_parameter(parameters, param_mode : str):
        for parameter_name, value_var in parameters:
            value = value_var.get()
            db.upsert_parameter_value(username = getUser(), mode = param_mode, parameter = parameter_name, value = value)

    def increment_counter(self, value_var1, max_val, param,param_increment):
        current_value1 = value_var1.get()
        if((param == "Lower Rate Limit") and (50<=current_value1<90)):
            increment_val = 1
        else:
            increment_val = param_increment

        if current_value1 < max_val:
            new_value_increment =  round(current_value1 + increment_val,1) # query from database
        else:
            messagebox.showinfo('Inavlid', 'Trying to go outside of range')
            new_value_increment =  round(current_value1,1)
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
            messagebox.showinfo('Invalid', 'Trying to go outside of range')
            new_value_decrement = round(current_value2,1)
        value_var2.set(new_value_decrement)
    
    def save_parameters(self, param_tuple, mode: Mode):
        # Save all processed parameters
        parameters = [(param_name, value_var) for param_name, value_var in param_tuple]
        ParameterProcess.process_parameter(parameters, mode)


class ProcessMode(tk.Frame, ParameterProcess):
    def __init__(self, parent: tk.Frame, mode: Mode):
        super().__init__(parent)
        self.mode_object: Mode = mode
        self.mode: str = mode.get_mode()
        self.subtitle: str = mode.get_subtitle()
        self.parameters: list = mode.get_parameters()
        self.set_display()

    def set_display(self):
        """Sets the display for the mode page."""

        # Set the title and subtitle
        tk.Label(self, text=f"Mode: {self.mode}", font=('Arial', 23)).grid(row=1, column=0, padx=(50, 0))
        tk.Label(self, text=self.subtitle, font=('Arial', 12)).grid(row=2, column=0, padx=(50, 0), pady=(0, 10))

        self.parameter_tuples: list(tuple) = []
        i = 0; row = 5

        # Set up buttons and labels for each parameter
        for param_name, param_value in self.parameters:
            # Initialize the parameter value variable to display
            value = tk.DoubleVar(self)
            value.set(param_value)
            self.parameter_tuples.append((param_name, value))

            # Parameter label
            label = tk.Label(self, text=f" {param_name}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))

            # Decrement button
            decrement_button = tk.Button(self, text="-", command = lambda v = value, i = i: \
                                         self.decrement_counter(v, self.mode_object.min_list[i],
                                                                 self.mode, self.mode_object.increment_list[i]))
            decrement_button.grid(row=row, column=0, padx=(0, 100))

            # Increment button
            increment_button = tk.Button(self, text="+", command = lambda v =value, i = i: \
                                         self.increment_counter(v, self.mode_object.max_list[i],self.parameter_tuples[i][0],
                                                                self.mode_object.increment_list[i]))
            increment_button.grid(row=row, column=0, padx=(100, 0))

            # Parameter value
            parameter_value = tk.Label(self, textvariable=value, font=('Arial', 16))
            parameter_value.grid(row=row, column=0, padx=(20, 20))   # Adjusted column for the label
            
            # Process button
            process_button = tk.Button(self, text=f"Process", command=lambda p=param_name, v=value, 
                                       m=self.mode: (self.mode_object.send_params_serial(),
                                                            ParameterProcess.process_parameter([(p,v)],m)))
            process_button.grid(row=row, column=0,padx=(300, 50))

            row+=1; i+=1

        # Save button
        save_button = tk.Button(self, text="Save", command = lambda p=self.parameter_tuples, 
                                m=self.mode: (self.mode_object.send_params_serial(), self.save_parameters(p, m)))
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
    
    
class AOO(Mode):
    def __init__(self):
        Mode.__init__(self, mode="AOO", 
                        subtitle="Atrium Paced | No chamber sensed | No response to sensing ")
        
class VOO(Mode):
    def __init__(self):
        Mode.__init__(self, mode="VOO", 
                        subtitle="Ventricle Paced | No chamber sensed | No response to sensing ")
        
class AAI(Mode):
    def __init__(self):
        Mode.__init__(self, mode="AAI", 
                        subtitle="Atrium Paced | Atrium Sensed | Inhibited response to sensing ")

class VVI(Mode):
    def __init__(self):
        Mode.__init__(self, mode="VVI", 
                        subtitle="Ventricle Paced | Ventricle Sensed | Inhibited response to sensing ")

class AOOR(Mode):
    def __init__(self):
        Mode.__init__(self, mode="AOOR", 
                        subtitle="Atrium Paced | No chamber sensed | Rate response to activity ")

class VOOR(Mode):
    def __init__(self):
        Mode.__init__(self, mode="VOOR", 
                        subtitle="Ventricle Paced | No chamber sensed | Rate response to activity ")

class AAIR(Mode):
    def __init__(self):
        Mode.__init__(self, mode="AAIR", 
                        subtitle="Atrium Paced | Atrium Sensed | Rate response to activity ")
        
class VVIR(Mode):
    def __init__(self):
        Mode.__init__(self, mode="VVIR", 
                        subtitle="Ventricle Paced | Ventricle Sensed | Rate response to activity ")