import tkinter as tk
from database.PacemakerDatabase import *
from account.LoginPage import *

db = PacemakerDatabase.get_instance
class ParameterProcess:
    def process_parameter(parameter_name, value_var,mode):
        # Retrieve the input value for the specified parameter
        value = value_var.get()
        # Process the value (replace this with your processing logic)
        print(f"Processing {parameter_name}: {value}")
        db.upsert_parameter_value(username = getUser,mode=mode, parameter=parameter_name,value=value)


class AOO(ParameterProcess,tk.Frame):
    def __init__(self,parent):
        lowerRateLimit_AOO = tk.StringVar()
        upperRateLimit_AOO = tk.StringVar()
        atrialAmplitude_AOO = tk.StringVar()
        atrialPulse_Width_AOO = tk.StringVar()
        super().__init__(parent)
        
        tk.Label(self, text="Mode: AOO", font = ('Arial',23)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Atrium Paced | No chamber sensed | No response to sensing ", 
                 font = ('Arial',12)).grid(row=2,column=0,padx=(50,0),pady=(0,10))
        
        # Create Entry widgets for parameters
        self.param_entries = {}
        self.parameter_values = {}
        """
        parameters = [
            ("Lower rate limit", lowerRateLimit_AOO),
            ("Upper rate limit",upperRateLimit_AOO),
            ("Atrial amplitude",atrialAmplitude_AOO),
            ("Atrial pulse width",atrialPulse_Width_AOO)
        ]"""

        parameters = db.get_parameters(mode ="AOO")

        row = 5  # Starting row for parameters
        for param, value_var in parameters:
            label = tk.Label(self, text=f" {param}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))
            entry = tk.Entry(self, textvariable=value_var)
            entry.grid(row=row, column=0, padx=(50, 0))  # Use padx to adjust the spacing
            self.param_entries[param] = entry

            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param, v=value_var: ParameterProcess.process_parameter(p, v))
            process_button.grid(row=row, column=0,padx=(300, 50))  # Place the button in a separate column
            row += 1
        
        tk.Label(self, text="Device:", font=('Arial', 10)).grid(row=30, column=0, padx=(0, 550), pady=(140, 0))
        tk.Label(self, text="[Show status + Device ID]", font=('Arial', 9)).grid(row=31, column=0, padx=(0, 450), pady=(0, 0))

        self.pack()
        
class VOO(tk.Frame):
    def __init__(self,parent):
        lowerRateLimit_VOO = tk.StringVar()
        upperRateLimit_VOO = tk.StringVar()
        ventricularAmplitude_VOO = tk.StringVar()
        VentricularPulseWidth_VOO = tk.StringVar()

        super().__init__(parent)
        tk.Label(self, text="MODE: VOO", font = ('Arial',20)).grid(row = 1, column=0, padx=(70,0))
        tk.Label(self, text="Ventrical Paced | No chamber sensed | No response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(70,0),pady=(0,10))
        
        # Create Entry widgets for parameters
        self.param_entries = {}
        self.parameter_values = {}
        parameters = [
            ("Lower rate limit", lowerRateLimit_VOO),
            ("Upper rate limit",upperRateLimit_VOO),
            ("Ventricular amplitude",ventricularAmplitude_VOO),
            ("Ventricular pulse width",VentricularPulseWidth_VOO)
        ]
        
        row = 5  # Starting row for parameters
        for param, value_var in parameters:
            label = tk.Label(self, text=f" {param}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))
            entry = tk.Entry(self, textvariable=value_var)
            entry.grid(row=row, column=0, padx=(50, 0) )  # Use padx to adjust the spacing
            self.param_entries[param] = entry

            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param, v=value_var: ParameterProcess.process_parameter(p, v))
            process_button.grid(row=row, column=0, padx=(300, 50))
            row += 1

        tk.Label(self, text="Device:",font = ('Arial',10)).grid(row = 30, column=0, padx=(0,550),pady=(140,0))
        tk.Label(self, text="[Show status + Device ID]",font = ('Arial',9)).grid(row = 31, column=0, padx=(0,450),pady=(0,0))
        

        self.pack()


class AAI (tk.Frame):
    def __init__(self,parent):
        lowerRateLimit_AAI = tk.StringVar()
        upperRateLimit_AAI = tk.StringVar()
        atrialAmplitude_AAI = tk.StringVar()
        atrialPulse_Width_AAI = tk.StringVar()
        atrialSensitivity_AAI = tk.StringVar()
        arp_AAI = tk.StringVar()
        pvarp_AAI = tk.StringVar()
        hystersis_AAI = tk.StringVar()
        rateSmoothing_AAI = tk.StringVar()
        
        super().__init__(parent)
        tk.Label(self, text="Mode: AAI", font = ('Arial',20)).grid(row = 1, column=0, padx=(70,0))
        tk.Label(self, text="Atrium Paced | Atrium chamber sensed | Inhibited response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(70,0), pady=(0,10))
        
        # Create Entry widgets for parameters
        self.param_entries = {}
        self.parameter_values = {}
        parameters = [
            ("Lower rate limit", lowerRateLimit_AAI),
            ("Upper rate limit",upperRateLimit_AAI),
            ("Atrial amplitude",atrialAmplitude_AAI),
            ("Atrial pulse width",atrialPulse_Width_AAI),
            ("Atrial sensitivity",atrialSensitivity_AAI),
            ("ARP",arp_AAI),
            ("PVARP",pvarp_AAI),
            ("Hystersis",hystersis_AAI),
            ("Rate Smoothing",rateSmoothing_AAI)
        
        ]
        row = 5  # Starting row for parameters
        for param, value_var in parameters:
            label = tk.Label(self, text=f" {param}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))
            entry = tk.Entry(self, textvariable=value_var)
            entry.grid(row=row, column=0, padx=(50, 0) )  # Use padx to adjust the spacing
            self.param_entries[param] = entry

            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param, v=value_var: ParameterProcess.process_parameter(p, v))
            process_button.grid(row=row, column=0, padx=(300, 50))
            row += 1
       
        tk.Label(self, text="Device:",font = ('Arial',10)).grid(row = 30, column=0, padx=(0,550),pady=(20,0))
        tk.Label(self, text="[Show status + Device ID]",font = ('Arial',9)).grid(row = 31, column=0, padx=(0,450),pady=(0,0))
        
        self.pack()

class VVI(tk.Frame):
    def __init__(self,parent):
        lowerRateLimit_VVI = tk.StringVar()
        upperRateLimit_VVI = tk.StringVar()
        ventricularAmplitude_VVI = tk.StringVar()
        ventricularPulse_Width_VVI = tk.StringVar()
        ventricularSensitivity_VVI = tk.StringVar()
        vrp_VVI = tk.StringVar()
        hystersis_VVI = tk.StringVar()
        rateSmoothing_VVI = tk.StringVar()

        super().__init__(parent)
        tk.Label(self, text="Mode: VVI", font = ('Arial',20)).grid(row = 1, column=0, padx=(50,0))
        tk.Label(self, text="Ventricle Paced | Ventricle chambers sensed | Inhibited response to sensing ", font = ('Arial',13)).grid(row=2,column=0,padx=(0,0),pady=(0,10))

        # Create Entry widgets for parameters
        self.param_entries = {}
        self.parameter_values = {}
        parameters = [
            ("Lower rate limit", lowerRateLimit_VVI),
            ("Upper rate limit",upperRateLimit_VVI),
            ("Ventricular amplitude",ventricularAmplitude_VVI),
            ("Ventricular pulse width",ventricularPulse_Width_VVI),
            ("Ventricular sensitivity",ventricularSensitivity_VVI),
            ("VRP",vrp_VVI),
            ("Hystersis",hystersis_VVI),
            ("Rate Smoothing",rateSmoothing_VVI)
        
        ]
        row = 5  # Starting row for parameters
        for param, value_var in parameters:
            label = tk.Label(self, text=f" {param}", font=('Arial', 12))
            label.grid(row=row, column=0, sticky="w", padx=(0, 0))
            entry = tk.Entry(self, textvariable=value_var)
            entry.grid(row=row, column=0, padx=(50, 0) )  # Use padx to adjust the spacing
            self.param_entries[param] = entry

            # Add a button for each parameter
            process_button = tk.Button(self, text=f"Process", command=lambda p=param, v=value_var: ParameterProcess.process_parameter(p, v))
            process_button.grid(row=row, column=0, padx=(300, 50))
            row += 1



        tk.Label(self, text="Device:",font = ('Arial',10)).grid(row = 30, column=0, padx=(0,550),pady=(35,0))
        tk.Label(self, text="[Show status + Device ID]",font = ('Arial',9)).grid(row = 31, column=0, padx=(0,450),pady=(0,0))

        self.pack()

