import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import json
import os
import math
import datetime
import customtkinter

def show_log():
    log_window = tk.Toplevel(root)
    log_window.title("Graph Log")
    log_window.attributes("-topmost", True)  # Set log window to always stay on top

    log_text = tk.Text(log_window, wrap=tk.WORD)
    log_text.pack(fill=tk.BOTH, expand=True)

    def update_log():
        # Read contents of log file and display in text widget
        with open("graph_log.txt", "r") as log_file:
            log_entries = log_file.readlines()
            log_text.config(state=tk.NORMAL)  # Enable editing temporarily
            log_text.delete("1.0", tk.END)  # Clear existing content
            log_text.insert(tk.END, "".join(log_entries))
            log_text.config(state=tk.DISABLED)  # Disable editing again

        # Schedule the next update
        log_window.after(1000, update_log)

    # Call update_log function to start updating the log
    update_log()

def log_graphs(interval, length):
    log_entry = f"Graphs shown at {datetime.datetime.now()}\n"
    log_entry += f"Interval: {interval}, Length: {length}\n\n"

    # Read existing contents of log file
    with open("graph_log.txt", "r") as log_file:
        existing_logs = log_file.read()

    # Prepend new log entry to existing logs
    updated_logs = log_entry + existing_logs

    # Write updated logs back to file
    with open("graph_log.txt", "w") as log_file:
        log_file.write(updated_logs)

def show_graphs():
    global canvas1, canvas2

    # Clear any existing graphs
    if canvas1:
        canvas1.get_tk_widget().destroy()
    if canvas2:
        canvas2.get_tk_widget().destroy()

    # Get interval and length of x-axis from entry widgets
    interval = float(interval_entry.get().replace(',','.'))
    length = int(length_entry.get().replace(',', '.'))

    log_graphs(interval, length)

    # Generate x values
    x_values1 = np.arange(0, (length * (1/interval)) * interval, interval)
    x_values2 = np.arange(0, (length  * (1/interval)) * interval, interval)

    # Generate y values (example values)
    y_values1 = np.sin(x_values1)
    y_values2 = np.cos(x_values2)

    # Create first graph
    fig1, ax1 = plt.subplots()
    ax1.plot(x_values1, y_values1)
    ax1.set_xlabel('X Label')
    ax1.set_ylabel('Y Label')
    ax1.set_title('Graph 1')

    # Display first graph on tkinter window
    canvas1 = FigureCanvasTkAgg(fig1, master=root)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Create second graph
    fig2, ax2 = plt.subplots()
    ax2.plot(x_values2, y_values2)
    ax2.set_xlabel('X Label')
    ax2.set_ylabel('Y Label')
    ax2.set_title('Graph 2')

    # Display second graph on tkinter window
    canvas2 = FigureCanvasTkAgg(fig2, master=root)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

def open_impressum_window():
    impressum_window = tk.Toplevel(root)
    impressum_window.title("Impressum")

    impressum_text = tk.Text(impressum_window, wrap=tk.WORD)
    impressum_text.pack(fill=tk.BOTH, expand=True)

    # Insert impressum text
    impressum_text.insert(tk.END, "Description of the App:\n")
    impressum_text.insert(tk.END, "This app provides a dashboard for the CCCP Space Project.\n\n")

    impressum_text.insert(tk.END, "CEO:\n")
    impressum_text.insert(tk.END, "Maximilian Schmidt\n\n")

    impressum_text.insert(tk.END, "Backend Developer:\n")
    impressum_text.insert(tk.END, "Sara Wagner Villadangos\n\n")

    impressum_text.insert(tk.END, "Frontend Developer:\n")
    impressum_text.insert(tk.END, "Sebastian Leo Morawietz\n\n")

    impressum_text.insert(tk.END, "UI:\n")
    impressum_text.insert(tk.END, "Nishant Rostewitz\n\n")

    impressum_text.insert(tk.END, "Tastenkombination:\n")
    impressum_text.insert(tk.END, "Strg+S - Speichern\n")
    impressum_text.insert(tk.END, "Strg+L - Datei Importieren\n")
    impressum_text.insert(tk.END, "F5     - Ausführen\n")
    impressum_text.insert(tk.END, "F11    - Vollbild\n")


    # Disable editing
    impressum_text.config(state=tk.DISABLED)

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def load_selected_settings(event=None):
    filename = selected_file_var.get()
    if filename:
        with open(os.path.join("./savings", filename + ".json"), "r") as f:
            settings = json.load(f)
            interval_entry.delete(0, tk.END)
            interval_entry.insert(0, settings["interval"])
            length_entry.delete(0, tk.END)
            length_entry.insert(0, settings["length"])
            print("Settings loaded successfully.")
            show_graphs()  # Update graphs after loading settings


def update_files_dropdown():
    default_dir = "./savings"
    json_files = [os.path.splitext(file)[0] for file in os.listdir(default_dir) if file.endswith(".json")]
    files_dropdown['values'] = json_files


def save_settings():
    settings = {
        "interval": interval_entry.get(),
        "length": length_entry.get()
    }
    default_dir = "./savings"
    os.makedirs(default_dir, exist_ok=True)
    filename = filedialog.asksaveasfilename(initialdir=default_dir, defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if filename:
        with open(filename, "w") as f:
            json.dump(settings, f)
            print("Settings saved successfully.")
    update_files_dropdown()  # Update dropdown after saving settings

def load_settings():
    filename = filedialog.askopenfilename(initialdir="./savings", filetypes=[("JSON Files", "*.json")])
    if filename:
        with open(filename, "r") as f:
            settings = json.load(f)
            interval_entry.delete(0, tk.END)
            interval_entry.insert(0, settings["interval"])
            length_entry.delete(0, tk.END)
            length_entry.insert(0, settings["length"])
            print("Settings loaded successfully.")
            update_files_dropdown()  # Update dropdown after loading settings
            selected_file_var.set(os.path.splitext(os.path.basename(filename))[0])
            show_graphs()  # Update graphs after loading settings

def interval_length_changed(event=None):
    selected_file_var.set("")

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Create main window
root = customtkinter.CTk()
root.title("CCCP Space Project Dashboard")  # Title added here
root.state('zoomed')
root.bind("<F11>", lambda event: root.toggle_fullscreen())
root.bind("<Control-s>", lambda event: save_settings())
root.bind("<Control-l>", lambda event: load_settings())
root.bind("<F5>", lambda event: show_graphs())

# Title label
title_label = ttk.Label(root, text="CCCP Space Project Dashboard", font=("Segoe UI", 20))
title_label.pack()  # Centered horizontally

# Full-screen button
fullscreen_button = customtkinter.CTkButton(root, text="⛶", command=toggle_fullscreen)
fullscreen_button.pack(side=tk.TOP, anchor=tk.NE, padx=5, pady=5)

# Dropdown menu for selecting settings file
selected_file_var = tk.StringVar()
files_dropdown = ttk.Combobox(root, values=selected_file_var, state="readonly")
files_dropdown.pack(side=tk.TOP, padx=5, pady=5)
files_dropdown.bind("<<ComboboxSelected>>", load_selected_settings)
update_files_dropdown()

# Initialize canvas widgets as None
canvas1 = None
canvas2 = None

# Create entry widgets for interval and length of x-axis
interval_label = ttk.Label(root, text="Interval between points:")
interval_label.pack()
interval_entry = customtkinter.CTkEntry(root)
interval_entry.insert(0, "0.1")  # Default interval
interval_entry.pack()
interval_entry.bind("<KeyRelease>", interval_length_changed)

length_label = ttk.Label(root, text="Length of x-axis:")
length_label.pack()
length_entry = customtkinter.CTkEntry(root)
length_entry.insert(0, "50")  # Default length
length_entry.pack()
length_entry.bind("<KeyRelease>", interval_length_changed)

# Create a button
button = customtkinter.CTkButton(root, text="Show Graphs", command=show_graphs)
button.pack()

# Footer frame
footer_frame = ttk.Frame(root)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Impressum button
impressum_button = customtkinter.CTkButton(footer_frame, text="Impressum", command=open_impressum_window)
impressum_button.pack(side=tk.LEFT)

# Save settings button
save_button = customtkinter.CTkButton(footer_frame, text="Save Settings", command=save_settings)
save_button.pack(side=tk.LEFT, padx=(5, 0))

# Load settings button
load_button = customtkinter.CTkButton(footer_frame, text="Load Settings", command=load_settings)
load_button.pack(side=tk.RIGHT, padx=(5, 0))

# Button to show log
show_log_button = customtkinter.CTkButton(footer_frame, text="Show Log", command=show_log)
show_log_button.pack(side=tk.RIGHT)

# Run the CustomTkinter event loop
root.mainloop()
