import serial
import struct

def write(port='COM6', baudrate=115200, timeout=0):
    # write an array of data
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        print("Writing", ser.write(set_parameters(RECEIVE = False, MODE = 3)), "bytes")        

def read(port='COM6', baudrate=115200, timeout=0) -> tuple:
    with serial.Serial(port, baudrate, timeout=timeout) as ser:
        ser.write(set_parameters(RECEIVE = True))
        while ser.in_waiting != 16:
            continue
        read_data = ser.read(ser.in_waiting)
        unpacked_signals = struct.unpack('<dd', read_data)
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
    parameters = struct.pack('<BBBHHHffHHHffHHHHHd', STANDARD, GIVE_PARAMS, MODE, LRL, URL, 
                             ARP_DELAY, ATR_AMP, VENT_AMP, VRP_DELAY, ATR_PW, VENT_PW,
                             ATR_SENSE, VENT_SENSE, VARP, MAX_SR, REACT_TIME, RESP_FACTOR,
                             REC_TIME, ACTIVITY_THRES)
    return parameters

if __name__ == '__main__':
    read()

    # parameters pack translation:
    # uint8 = B
    # uint16 = H
    # single = f
    # double = d

# Using the parameters pack translation, translate following:

# MODE = typecast(Rx(3),'uint8');
# LRL = typecast(Rx(4:5),'uint16');
# URL =typecast(Rx(6:7),'uint16');
# ARP_DELAY  = typecast(Rx(8:9),'uint16');
# ATR_AMP = typecast(Rx(10:13),'single');
# VENT_AMP= typecast(Rx(14:17),'single');
# VRP_DELAY= typecast(Rx(18:19),'uint16');
# ATR_PW= typecast(Rx(20:21),'uint16');
# VENT_PW = typecast(Rx(22:23),'uint16');
# ATR_SENSE = typecast(Rx(24:27), 'single');
# VENT_SENSE = typecast(Rx(28:31), 'single');
# PVARP = typecast(Rx(32:33), 'uint16');
# MAX_SR = typecast(Rx(34:35), 'uint16');
# REACT_TIME = typecast(Rx(36:37),'uint16');
# RESP_FACTOR =  typecast(Rx(38:39),'uint16');
# REC_TIME =  typecast(Rx(40:41),'uint16');
# ACTIVITY_THRES =  typecast(Rx(42:49),'double');

# '<BHHHffHHHffHHHHHd'
# sum the bytes used:
# 1 + 2 + 2 + 2 + 4 + 4 + 2 + 2 + 2 + 4 + 4 + 2 + 2 + 2 + 2 + 2 + 8 = 49 bytes


# For receiving data, use the following:
# LRL = typecast(Rx(4:5),'uint16'); H
# URL =typecast(Rx(6:7),'uint16'); H
# MODE = typecast(Rx(3),'uint8'); B
# ARP_DELAY  = typecast(Rx(8:9),'uint16'); H
# ATR_PW= typecast(Rx(20:21),'uint16'); H
# VENT_PW = typecast(Rx(22:23),'uint16'); H
# ATR_AMP = typecast(Rx(10:13),'single'); f
# VENT_AMP= typecast(Rx(14:17),'single'); f
# VRP_DELAY= typecast(Rx(18:19),'uint16'); H
# PVARP = typecast(Rx(32:33), 'uint16'); H
# MAX_SR = typecast(Rx(34:35), 'uint16'); H
# REACT_TIME = typecast(Rx(36:37),'uint16'); H
# RESP_FACTOR =  typecast(Rx(38:39),'uint16'); H
# REC_TIME =  typecast(Rx(40:41),'uint16'); H
# ATR_SENSE = typecast(Rx(24:27), 'single'); f
# VENT_SENSE = typecast(Rx(28:31), 'single'); f
# ACTIVITY_THRES =  typecast(Rx(42:49),'double'); d
# ATR_SIGNAL = typecast(Rx(50:57),'double'); d
# VENT_SIGNAL = typecast(Rx(58:65),'double'); d

# '<HHBHHHffHHHHHHffddd'
# sum the bytes used:
# 2 + 2 + 1 + 2 + 2 + 2 + 4 + 4 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 4 + 4 + 4 + 8 + 8 = 63 bytes