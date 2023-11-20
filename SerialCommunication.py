import serial
import bitstring
import struct

def main(port='COM6', baudrate=115200, timeout=0):
    # write an array of data
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print("Sending:", params_as_bytes())
        print("Writing", ser.write(params_as_bytes()), "bytes")
        #  read until received 31 bytes
        print("Reading", ser.read_until(size=35), "bytes")



def params_as_bytes():
    params: bytearray  = []
    STANDARD: int = 22
    GIVE_PARAMS: int = 18
    TEST_PARAMS: int = 34
    MODE: int = 1  # VOO
    LRL: int = 50
    URL: int = 120
    ARP_DELAY: int = 200
    ATR_AMP: float = 3.5
    VENT_AMP: float = 2.0
    VRP_DELAY: int = 200
    ATR_PW: int = 10
    VENT_PW: int = 2
    ATR_THRESHOLD: float = 1.8
    VENT_THRESHOLD: float = 2.2
    # convert to bytes and append to params


    parameters = struct.pack('<BBBHHHffHHHff', STANDARD, GIVE_PARAMS, MODE, LRL, URL, 
                             ARP_DELAY, ATR_AMP, VENT_AMP, VRP_DELAY, ATR_PW, VENT_PW,
                              ATR_THRESHOLD, VENT_THRESHOLD)
    print(parameters)
    return parameters

def convert_to_bytes(num, bytes = 8):
    """Converts a number to a bitstring of length bytes*8"""
    if bytes == 8:
        return bitstring.BitArray(float=num, length=bytes*8).bytes
    return bitstring.BitArray(int=num, length=bytes*8).bytes
    
if __name__ == '__main__':
    main()
    # print(params_as_bytes())
