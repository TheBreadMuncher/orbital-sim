
import tkinter as tk
from tkinter import messagebox
from main import calculate_orbit

def calculate():
    try:
        altitude = float(entry_altitude.get())
        latitude = float(entry_latitude.get())
        radius, period_sec = calculate_orbit(altitude, latitude)
        period_hr = period_sec / 3600
        result_label.config(
            text=f"Orbital Radius: {radius/1000:.2f} km\nOrbital Period: {period_hr:.2f} hours"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

root = tk.Tk()
root.title("OrbitalSim GUI")
root.geometry("400x250")

tk.Label(root, text="Enter Altitude (km):").pack(pady=5)
entry_altitude = tk.Entry(root)
entry_altitude.pack()

tk.Label(root, text="Enter Latitude (°):").pack(pady=5)
entry_latitude = tk.Entry(root)
entry_latitude.pack()

tk.Button(root, text="Calculate Orbit", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
