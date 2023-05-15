import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class ProjectileMotionGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Projectile Motion")

        # Create labels and entry boxes for input parameters
        self.label_velocity = tk.Label(self.master, text="Initial Velocity (m/s): ")
        self.label_velocity.grid(row=0, column=0, padx=10, pady=10)
        self.entry_velocity = tk.Entry(self.master)
        self.entry_velocity.grid(row=0, column=1, padx=10, pady=10)

        self.label_angle = tk.Label(self.master, text="Launch Angle (degrees): ")
        self.label_angle.grid(row=1, column=0, padx=10, pady=10)
        self.entry_angle = tk.Entry(self.master)
        self.entry_angle.grid(row=1, column=1, padx=10, pady=10)

        # Create button for plotting trajectory
        self.button_plot = tk.Button(self.master, text="Plot", command=self.plot_trajectory)
        self.button_plot.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Create a figure and canvas for embedding the plot
        self.figure = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def plot_trajectory(self):
        # Get input parameters from entry boxes
        velocity = float(self.entry_velocity.get())
        angle = float(self.entry_angle.get())

        # Convert angle to radians
        angle_rad = np.deg2rad(angle)

        # Calculate time of flight
        time_of_flight = (2 * velocity * np.sin(angle_rad)) / 9.8

        # Calculate horizontal and vertical distances
        t = np.linspace(0, time_of_flight, num=100)
        x = velocity * np.cos(angle_rad) * t
        y = velocity * np.sin(angle_rad) * t - 0.5 * 9.8 * t ** 2

        # Clear the previous plot
        self.figure.clear()

        # Create a new plot
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel('Horizontal Distance (m)')
        ax.set_ylabel('Vertical Distance (m)')
        ax.set_title('Projectile Motion')
        ax.grid(True)

        # Update the canvas
        self.canvas.draw()

# Create tkinter window
root = tk.Tk()
root.title("Projectile Motion")

# Create ProjectileMotionGUI instance
projectile_motion_gui = ProjectileMotionGUI(root)

# Run tkinter event loop
root.mainloop()
