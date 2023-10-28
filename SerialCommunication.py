import serial

def open_port1():
    """Open port at “9600,8,N,1”, no timeout:"""
    ser = serial.Serial('/dev/ttyUSB0')     # open serial port
    print(ser.name)                         # check which port was really used
    ser.write(b'hello')                     # write a string
    ser.close()                             # close port

def open_port2():
    """Open named port at "19200, 8 N, 1", 1s timeout:"""
    with serial.Serial('/dev/ttyS1', 19200, timeout=1) as ser:
        x = ser.read()          # read one byte
        s = ser.read(10)        # read up to ten bytes (timeout)
        line = ser.readline()   # read a '\n' terminated line

def open_port3():
    """Open port at “38400,8,E,1”, non blocking HW handshaking:"""
    ser = serial.Serial('COM3', 38400, timeout=0,
    parity=serial.PARITY_EVEN, rtscts=1)
    s = ser.read(100) # read up to one hundred bytes
    # or as much is in the buffer

if __name__ == '__main__':
    open_port1()