from collections import deque
from datetime import *

class egram():
    __timeline: deque = None

    def __init__(self):
        self.__timeline = deque()

    def __str__(self):
        return str(self.__timeline)

    def append_milliVolts(self, milliVolts: float):
        time = datetime.now()
        min = time.minute
        sec = time.second
        microSec = time.microsecond 
        self.__timeline.append(((min, sec, microSec), milliVolts))

    def pop(self):
        return self.__timeline.pop()
    
    def popleft(self):
        return self.__timeline.popleft()
    
    def length(self):
        return len(self.__timeline)
    
    def isEmpty(self):
        return len(self.__timeline) == 0
    
e = egram()
b = e.isEmpty()
e.append_milliVolts(3)
e.append_milliVolts(4)
e.append_milliVolts(5)
e.append_milliVolts(9)
e.append_milliVolts(0)
print(e)
    