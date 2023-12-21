import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# Global variables for storing data
force_data = []
deformation_data = []
time_data = []

# Function to open CSV file and load data
def open_csv():
    global force_data, deformation_data, time_data
    file_path = filedialog.askopenfilename()
    try:
        df = pd.read_csv(file_path)
        deformation_data = df['mm'].tolist()
        force_data = df['kN'].tolist()
        
        time_data = df['Time(sec)'].tolist()
        label_result.config(text="CSV successfully loaded!")
    except Exception as e: 
        label_result.config(text="Failed to load CSV file.")
        print(e)

# Function to plot force vs deformation
def plot_force_deformation():
    global force_data, deformation_data
    plt.plot(deformation_data, force_data)
    plt.xlabel('Deformation (mm)')
    plt.ylabel('Force (kN)')
    plt.title('Force vs Deformation')
    plt.grid(True)
    plt.show()

# Function to plot force vs time
def plot_force_time():
    global force_data, time_data
    plt.plot(time_data, force_data)
    plt.xlabel('Time (sec)')
    plt.ylabel('Force (kN)')
    plt.title('Force vs Time')
    plt.grid(True)
    plt.show()

# Create GUI window
root = tk.Tk()
root.title("CSV Data Visualization")
root.geometry("400x400")

# Create labels and entry fields for user input
label_instruction = tk.Label(root, text="Please load a CSV file with 3 columns: 'mm', 'kN', and 'Time(sec)'")
label_instruction.pack(pady=10)

# Create buttons
button_open_csv = tk.Button(root, text="Open CSV", command=open_csv)
button_open_csv.pack(pady=10)

button_plot_force_deformation = tk.Button(root, text="Plot Force vs Deformation", command=plot_force_deformation)
button_plot_force_deformation.pack(pady=10)

button_plot_force_time = tk.Button(root, text="Plot Force vs Time", command=plot_force_time)
button_plot_force_time.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack()

# Run the GUI event loop
root.mainloop()
