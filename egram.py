from collections import deque
from datetime import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import SerialCommunication as sc
import threading

class egram():

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.signals = []
        self.timestamps = []

    def animate_signal_helper(self, i, signal_index: int):
        # Read pacemaker signals
        signals = sc.read()
        signal = signals[signal_index]

        # Add x and y to lists
        self.signals.append(signal)
        self.timestamps.append(datetime.now())
        
        # Limit x and y lists to 100 items
        self.signals = self.signals[-100:]
        self.timestamps = self.timestamps[-100:]

        # Draw x and y lists
        self.ax.clear()
        self.ax.plot(self.timestamps, self.signals)

        # Format plot
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(bottom=0.30)
        if signal_index == 0:
            plt.title('Atrium')
        else:
            plt.title('Ventricle')
        plt.xlabel('Time')
        plt.ylabel('Voltage')

    def animate_atr(self, i):
        self.animate_signal_helper(i, 0)

    def animate_vent(self, i):
        self.animate_signal_helper(i, 1)
    
    def display_atr_egram(self):
        self.ani = animation.FuncAnimation(self.fig, self.animate_atr, interval=10)
        plt.show()
    
    def display_vent_egram(self):
        self.ani = animation.FuncAnimation(self.fig, self.animate_vent, interval=10)
        plt.show()
    
    def stop_animation(self):
        self.ani.event_source.stop()

    def animate_signals(self, i):
        """Animates both atrium and ventricle signals in subplots,
        with the atrium on top and the ventricle on the bottom"""
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        self.ax1 = ax1
        self.ax2 = ax2
        self.animate_atr(i)
        self.animate_vent(i)
        
        
if __name__ == '__main__':
    e = egram()
    e.display_atr_egram()