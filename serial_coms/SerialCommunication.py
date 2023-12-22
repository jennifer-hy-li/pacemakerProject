# Author: Jayden Hooper

import serial
import struct
import time
from serial_coms.ComsIndicator import *

PORT = 'COM8'
BAUDRATE = 115200
TIMEOUT = 0

def write(parameters, port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT):
    """Writes the parameters to the pacemaker.""" 
    # write an array of data
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        Indicator.get_instance().set_connection_status(True)
        time.sleep(0.3)
        print("Writing", ser.write(parameters), "bytes")
        Indicator.get_instance().set_connection_status(False)        

def read(port=PORT, baudrate=BAUDRATE, timeout=TIMEOUT) -> tuple:
    """Reads the egram data from the pacemaker"""
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        Indicator.get_instance().set_connection_status(True)
        ser.write(set_parameters(RECEIVE = True))
        while ser.in_waiting != 16:
            continue
        read_data = ser.read(ser.in_waiting)
        unpacked_signals = struct.unpack('<dd', read_data)
        Indicator.get_instance().set_connection_status(False)
        return unpacked_signals

def set_parameters(RECEIVE = False, MODE = 3, LRL = 60, URL = 120, ARP_DELAY = 200, 
                   ATR_AMP = 3.5, VENT_AMP = 3.5, VRP_DELAY = 200, 
                   ATR_PW = 10, VENT_PW = 10, ATR_SENSE = 80, 
                   VENT_SENSE = 80, VARP = 150, MAX_SR = 120,
                   REACT_TIME = 30, RESP_FACTOR = 8, REC_TIME = 30,
                   ACTIVITY_THRES = 0.5):
    """Sets the parameters for the pacemaker"""
    STANDARD: int = 22
    GIVE_PARAMS: int = 34 if RECEIVE else 18
    parameters = struct.pack('<BBBHHHffHHHffHHHHHd', STANDARD, GIVE_PARAMS, MODE, 
                             int(LRL), int(URL), int(ARP_DELAY), float(ATR_AMP), float(VENT_AMP),
                             int(VRP_DELAY), int(ATR_PW), int(VENT_PW), float(ATR_SENSE), 
                             float(VENT_SENSE), int(VARP), int(MAX_SR), int(REACT_TIME), 
                             int(RESP_FACTOR), int(REC_TIME), int(ACTIVITY_THRES)) # 16 variables
    return parameters

def get_parameter_map():
    """Returns a dictionary of the parameter 
    names to the short hand notation"""
    return {'MODE': 'MODE', 'Lower Rate Limit': 'LRL', 'Upper Rate Limit': 'URL',
            'ARP' : 'ARP_DELAY', 'Atrial Amplitude': 'ATR_AMP', 'Ventricular Amplitude': 'VENT_AMP',
            'VRP': 'VRP_DELAY', 'Atrial Pulse Width': 'ATR_PW', 'Ventricular Pulse Width': 'VENT_PW',
            'Atrial Sensitivity': 'ATR_SENSE', 'Ventricular Sensitivity': 'VENT_SENSE',
            'VRP': 'VARP', 'Maximum Sensor Rate': 'MAX_SR', 'Reaction Time': 'REACT_TIME',
            'Response Factor': 'RESP_FACTOR', 'Recovery Time': 'REC_TIME', 'Activity Threshold': 'ACTIVITY_THRES'}

def get_mode_number(mode):
    """Returns the mode number given the mode name"""
    return {'AOO': 1, 'AAI': 2, 'VOO': 3, 'VVI': 4, 
            'AOOR': 5, 'AAIR': 6, 'VOOR': 7, 'VVIR': 8}[mode]

if __name__ == '__main__':
    write(set_parameters(RECEIVE = False, MODE = 8))
