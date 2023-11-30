import serial
import struct

def write(port='COM6', baudrate=115200, timeout=0):
    # write an array of data
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print("Writing", ser.write(set_parameters(RECEIVE = False, MODE = 3)), "bytes")        

def read(port='COM6', baudrate=115200, timeout=0):
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print("Sending", ser.write(set_parameters(RECEIVE = True)), "bytes of read parameters")
        while True:
            if ser.in_waiting == 29:
                read_data = ser.read(ser.in_waiting)
                unpacked_data = struct.unpack('<HHBHHHffffH', read_data)
                break
        print("Successfully read data:", unpacked_data)

def set_parameters(RECEIVE = True, MODE = 3, LRL = 60, URL = 120, ARP_DELAY = 200, 
                   ATR_AMP = 3.5, VENT_AMP = 3.5, VRP_DELAY = 200, 
                   ATR_PW = 10, VENT_PW = 10, ATR_THRESHOLD = 80, 
                   VENT_THRESHOLD = 80):
    """Sets the parameters for the pacemaker"""
    STANDARD: int = 22
    GIVE_PARAMS: int = 34 if RECEIVE else 18
    parameters = struct.pack('<BBBHHHffHHHff', STANDARD, GIVE_PARAMS, MODE, LRL, URL, 
                             ARP_DELAY, ATR_AMP, VENT_AMP, VRP_DELAY, ATR_PW, VENT_PW,
                              ATR_THRESHOLD, VENT_THRESHOLD)
    return parameters

if __name__ == '__main__':
    read()