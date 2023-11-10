import serial
from pySerialTransfer import pySerialTransfer as txfer


def main(port='COM6', baudrate=9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1):
    # write an array of data
    with serial.Serial(port, baudrate, timeout=timeout, parity=parity, rtscts=rtscts) as ser:
        ser.write(b'hello world')

        ser = ser.read(100) # read up to one hundred bytes
        print(ser)   

if __name__ == '__main__':
    main()