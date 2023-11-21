import serial
import struct

def write(port='COM6', baudrate=115200, timeout=0):
    # write an array of data
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print("Writing", ser.write(set_parameters(MODE = 4)), "bytes")

def read(port='COM6', baudrate=115200, timeout=0):
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print("Sending", ser.write(send_read_parameters()), "bytes of read parameters")
        line = ser.read(35)
        if line:
            # line = struct.unpack('<BBBHHHffHHHff', line)   # <-- uncomment when data has been received
            print("Data received:", line)
        else:
            print("No data received:", line)

def set_parameters(MODE = 3, LRL = 60, URL = 120, ARP_DELAY = 200, 
                   ATR_AMP = 3.5, VENT_AMP = 3.5, VRP_DELAY = 200, 
                   ATR_PW = 10, VENT_PW = 10, ATR_THRESHOLD = 80, 
                   VENT_THRESHOLD = 80):
    """Sets the parameters for the pacemaker"""
    STANDARD: int = 22
    GIVE_PARAMS: int = 18
    parameters = struct.pack('<BBBHHHffHHHff', STANDARD, GIVE_PARAMS, MODE, LRL, URL, 
                             ARP_DELAY, ATR_AMP, VENT_AMP, VRP_DELAY, ATR_PW, VENT_PW,
                              ATR_THRESHOLD, VENT_THRESHOLD)
    return parameters

def send_read_parameters():
    """Reads the egram data from the pacemaker"""
    STANDARD: int = 22
    READ_EGRAM: int = 34
    data = struct.pack('<BB', STANDARD, READ_EGRAM)
    # data = struct.pack('<BBBHHHffHHHff', STANDARD, READ_EGRAM, 1, 60, 120, 1, 3.5, 3.5, 1, 10, 10, 1.8, 2.2) 
    return data

if __name__ == '__main__':
    write()