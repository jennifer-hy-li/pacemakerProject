# Author: Jayden Hooper

from collections import deque
from datetime import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import SerialCommunication as sc

class egram():

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.fig.canvas.mpl_connect('close_event', self.on_close)
        self.signals = []
        self.timestamps = []
        self.ani = None
    
    def on_close(self, event):
        """Stops the animation when the user closes the window."""
        if self.ani != None:
            self.ani.event_source.stop()

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
        self.ani.event_source.pause()
        
        
if __name__ == '__main__':
    e = egram()
    e.display_atr_egram()