from collections import deque
from datetime import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import SerialCommunication as sc

class egram():
    __time: deque = None
    __atr_timeline: deque = None
    __vent_timeline: deque = None

    def __init__(self):
        self.__time = deque()
        self.__atr_timeline = deque()
        self.__vent_timeline = deque()
    
    def append_signals(self, atr_milliVolts: float, vent_milliVolts: float):
        self.__time.append(datetime.now())
        self.__atr_timeline.append(atr_milliVolts)
        self.__vent_timeline.append(vent_milliVolts)

    # def pop(self):
    #     return self.__timeline.pop()
    
    # def popleft(self):
    #     return self.__timeline.popleft()
    
    # def length(self):
    #     return len(self.__timeline)
    
    # def isEmpty(self):
    #     return len(self.__timeline) == 0
    
    def display(self):
        # display 2 graphs, one for atrium and one for ventricle in subplots
        plt.subplot(2,1,1)
        plt.subplots_adjust(hspace=0.5)
        plt.plot(self.__time, self.__atr_timeline)
        plt.title('Atrium')
        plt.xlabel('Time')
        plt.ylabel('Voltage')
        plt.subplot(2,1,2)
        plt.plot(self.__time, self.__vent_timeline)
        plt.title('Ventricle')
        plt.xlabel('Time')
        plt.ylabel('Voltage')
        plt.show()

    def init_animation(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.xs = []
        self.ys = []

    def animate_atrium(self, i):
        signals = sc.read()
        atr_signal = signals[0]
        vent_signal = signals[1]

        # Add x and y to lists
        self.xs.append(datetime.now())
        self.ys.append(atr_signal)

        # Limit x and y lists to 20 items
        self.xs = self.xs[-100:]
        self.ys = self.ys[-100:]

        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(self.xs, self.ys)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        plt.title('Atrium')
        plt.xlabel('Time')
        plt.ylabel('Voltage')

    
e = egram()
e.init_animation()
ani = animation.FuncAnimation(e.fig, e.animate_atrium, interval=50)
plt.show()
    