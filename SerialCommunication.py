import serial
import bitstring
import struct
import time

def main(port='COM6', baudrate=115200, timeout=0):
    # write an array of data
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print("Sending:", set_parameters())
        print("Writing", ser.write(set_parameters()), "bytes")
        # sleep 10 seconds
        time.sleep(10)
        print("Writing", ser.write(set_parameters(LRL = 10)), "bytes")
        time.sleep(10)
        print("Writing", ser.write(set_parameters(MODE = 4)), "bytes")
        time.sleep(10)
        print("Writing", ser.write(set_parameters(MODE = 1)), "bytes")
        time.sleep(10)
        print("Writing", ser.write(set_parameters(MODE = 2)), "bytes")
        print("Reading", read_egram_data(), "bytes")

def set_parameters(MODE = 3, LRL = 60, URL = 120, ARP_DELAY = 1, 
                   ATR_AMP = 3.5, VENT_AMP = 3.5, VRP_DELAY = 1, 
                   ATR_PW = 10, VENT_PW = 10, ATR_THRESHOLD = 1.8, 
                   VENT_THRESHOLD = 2.2):
    """Sets the parameters for the pacemaker"""
    STANDARD: int = 22
    GIVE_PARAMS: int = 18
    parameters = struct.pack('<BBBHHHffHHHff', STANDARD, GIVE_PARAMS, MODE, LRL, URL, 
                             ARP_DELAY, ATR_AMP, VENT_AMP, VRP_DELAY, ATR_PW, VENT_PW,
                              ATR_THRESHOLD, VENT_THRESHOLD)
    return parameters

def read_egram_data():
    """Reads the egram data from the pacemaker"""
    STANDARD: int = 22
    READ_EGRAM: int = 34
    data = struct.pack('<BB', STANDARD, READ_EGRAM)
    return data

def convert_to_bytes(num, bytes = 8):
    """Converts a number to a bitstring of length bytes*8"""
    if bytes == 8:
        return bitstring.BitArray(float=num, length=bytes*8).bytes
    return bitstring.BitArray(int=num, length=bytes*8).bytes
    
if __name__ == '__main__':
    main()