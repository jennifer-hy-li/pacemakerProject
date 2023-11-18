import serial
import bitstring
import struct

def main(port='COM6', baudrate=115200, timeout=0):
    # write an array of data
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print("Sending:", params_as_bytes())
        print("Writing", ser.write(params_as_bytes()), "bytes")

def params_as_bytes():
    params: bytearray  = []
    GIVE_PARAMS1: int = 22
    GIVE_PARAMS2: int = 18
    MODE: int = 3  # VOO
    LRL: int = 60
    URL: int = 120
    ARP_DELAY: int = 200
    ATR_AMP: float = 3.5
    VENT_AMP: float = 3.5
    VRP_DELAY: int = 200
    ATR_PW: int = 10
    VENT_PW: int = 10
    ATR_THRESHOLD: float = 1.8
    VENT_THRESHOLD: float = 2.2
    # convert to bytes and append to params

    params.append(convert_to_bytes(GIVE_PARAMS1, 1))
    params.append(convert_to_bytes(GIVE_PARAMS2, 1))
    params.append(convert_to_bytes(MODE, 1))
    params.append(convert_to_bytes(LRL, 2))
    params.append(convert_to_bytes(URL, 2))
    params.append(convert_to_bytes(ARP_DELAY, 2))
    params.append(convert_to_bytes(ATR_AMP, 4))
    params.append(convert_to_bytes(VENT_AMP, 4))
    params.append(convert_to_bytes(VRP_DELAY, 2))
    params.append(convert_to_bytes(ATR_PW, 2))
    params.append(convert_to_bytes(VENT_PW, 2))
    params.append(convert_to_bytes(ATR_THRESHOLD, 4))
    params.append(convert_to_bytes(VENT_THRESHOLD, 4))

    parameters = struct.pack('<BBBHHHffHHHFF', GIVE_PARAMS1, GIVE_PARAMS2, MODE, LRL, URL, 
                             ARP_DELAY, ATR_AMP, VENT_AMP, VRP_DELAY, ATR_PW, VENT_PW,
                              ATR_THRESHOLD, VENT_THRESHOLD)
    return parameters

def convert_to_bytes(num, bytes = 8):
    """Converts a number to a bitstring of length bytes*8"""
    if bytes == 8:
        return bitstring.BitArray(float=num, length=bytes*8).bytes
    return bitstring.BitArray(int=num, length=bytes*8).bytes
    
if __name__ == '__main__':
    main()
