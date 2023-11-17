import serial
import bitstring

def main(port='COM6', baudrate=115200, timeout=0):
    # write an array of data
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print("Sending:", params_as_bytes())
        print("Writing", ser.write(params_as_bytes()), "bytes")

def params_as_bytes():
    params: bytes = []
    MODE: int = 2  # VOO
    LRL: int = 1
    URL: int = 1
    ARP_DELAY: int = 1
    ATR_AMP: float = 1
    VENT_AMP: float = 1
    VRP_DELAY: int = 1
    ATR_PW: int = 1
    VENT_PW: int = 1
    ATR_THRESHOLD: float = 1.0
    VENT_THRESHOLD: float = 1.0

    # convert to bytes and append to params
    params.append(convert_to_bytes(MODE, 1))
    params.append(convert_to_bytes(LRL, 1))
    params.append(convert_to_bytes(URL, 1))
    params.append(convert_to_bytes(ARP_DELAY, 8))
    params.append(convert_to_bytes(ATR_AMP, 8))
    params.append(convert_to_bytes(VENT_AMP, 8))
    params.append(convert_to_bytes(VRP_DELAY, 8))
    params.append(convert_to_bytes(ATR_PW, 8))
    params.append(convert_to_bytes(VENT_PW, 8))
    params.append(convert_to_bytes(ATR_THRESHOLD, 8))
    params.append(convert_to_bytes(VENT_THRESHOLD, 8))

    parameters: bytes = b''.join(params)
    return parameters

def convert_to_bytes(num, bytes = 8):
    """Converts a number to a bitstring of length bytes*8"""
    if bytes == 8:
        return bitstring.BitArray(float=num, length=bytes*8).bytes
    return bitstring.BitArray(int=num, length=bytes*8).bytes
    
if __name__ == '__main__':
    main()
