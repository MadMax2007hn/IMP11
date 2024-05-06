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
from tkinter import messagebox

def show_log():
	log_window = tk.Toplevel(root)
	log_window.title("Log-Datei")
	log_window.attributes("-topmost", True)  # Set log window to always stay on top
	log_window.iconbitmap("log.ico")

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
		log_window.after(500, update_log)

	# Call update_log function to start updating the log
	update_log()

def log_graphs(interval, length):
	log_entry = f"Graphen gezeigt um {datetime.datetime.now()}\n"
	log_entry += f"Interval: {interval}, Länge: {length}\n\n"

	# Read existing contents of log file
	with open("graph_log.txt", "r") as log_file:
		existing_logs = log_file.read()

	# Prepend new log entry to existing logs
	updated_logs = log_entry + existing_logs

	# Write updated logs back to file
	with open("graph_log.txt", "w") as log_file:
		log_file.write(updated_logs)


def log_error(interval, length, message):
	log_entry = f"ERROR: Versuch um {datetime.datetime.now()} mit dem Fehler: {message}\n"
	log_entry += f"Interval: {interval},  Länge: {length}\n\n"

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
	interval = interval_entry.get().replace(',','.')
	length = length_entry.get().replace(',', '.')

	#check if data is entered correctly and format
	#1. interval
	try:
		interval = float(interval)
	except:
		message = "Der Intervall muss eine Fließkommazahl sein"
		messagebox.showerror("Fehler", message)
		log_error(interval, length, message)
		return

	#2. length
	try:
		length = int(length)
	except:
		message = "Die Länge muss eine natürliche Zahl sein (1,2,3,4)"
		log_error(interval, length, message)
		messagebox.showerror("Fehler", message)
		return

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
	impressum_window.iconbitmap("impressum.ico")

	impressum_text = tk.Text(impressum_window, wrap=tk.WORD)
	impressum_text.pack(fill=tk.BOTH, expand=True)

	# Insert impressum text
	impressum_text.insert(tk.END, "Beschreibung der App:\n")
	impressum_text.insert(tk.END, "Hier kommt die Beschreibung unseres Projektes hin\n\n")

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
	update_files_dropdown()  # Update dropdown after saving settings
	selected_file_var.set(os.path.splitext(os.path.basename(filename))[0])

def load_settings():
	filename = filedialog.askopenfilename(initialdir="./savings", filetypes=[("JSON Files", "*.json")])
	if filename:
		with open(filename, "r") as f:
			settings = json.load(f)
			interval_entry.delete(0, tk.END)
			interval_entry.insert(0, settings["interval"])
			length_entry.delete(0, tk.END)
			length_entry.insert(0, settings["length"])
			update_files_dropdown()  # Update dropdown after loading settings
			selected_file_var.set(os.path.splitext(os.path.basename(filename))[0])
			show_graphs()  # Update graphs after loading settings

def interval_length_changed(event=None):
	selected_file_var.set("")

def empty_all():
    interval_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)

def reset_default():
    interval_entry.delete(0, tk.END)
    interval_entry.insert(0, "0.1")
    length_entry.delete(0, tk.END)
    length_entry.insert(0, "50")
    show_graphs()

# Create main window
root = tk.Tk()
root.title("CCCP Space Project")  # Title added here
#root.state('zoomed') #- does not work in Replit
root.minsize(1286,736)
root.bind("<F11>", lambda event: toggle_fullscreen())
root.bind("<Control-s>", lambda event: save_settings())
root.bind("<Control-l>", lambda event: load_settings())
root.bind("<F5>", lambda event: show_graphs())
root.bind("<F1>", lambda event: empty_all())
root.bind("<Control-r>", lambda event: reset_default())
root.iconbitmap("rakete.ico")


# Title label
title_label = ttk.Label(root, text="CCCP Space Project", font=("Segoe UI", 20))
title_label.pack()  # Centered horizontally

#Extra Setting Frame
extra_settings_frame= ttk.Frame(root)
extra_settings_frame.pack(side=tk.TOP, fill=tk.X)

# Full-screen button
fullscreen_button = ttk.Button(extra_settings_frame, text="⛶", command=toggle_fullscreen)
fullscreen_button.pack(side=tk.RIGHT, padx=10)

# Button to show log
show_log_button = ttk.Button(extra_settings_frame, text="Log Anzeigen", command=show_log)
show_log_button.pack(side=tk.RIGHT)

# Dropdown menu for selecting settings file
selected_file_var = tk.StringVar()
files_dropdown = ttk.Combobox(root, textvariable=selected_file_var, state="readonly")
files_dropdown.pack(side=tk.TOP, padx=5, pady=5)
files_dropdown.bind("<<ComboboxSelected>>", load_selected_settings)
update_files_dropdown()

# Initialize canvas widgets as None
canvas1 = None
canvas2 = None

# Create entry widgets for interval and length of x-axis
interval_label = ttk.Label(root, text="Interval:")
interval_label.pack()
interval_entry = ttk.Entry(root)
interval_entry.insert(0, "0.1")  # Default interval
interval_entry.pack()
interval_entry.bind("<KeyRelease>", interval_length_changed)

length_label = ttk.Label(root, text="Länge:")
length_label.pack()
length_entry = ttk.Entry(root)
length_entry.insert(0, "50")  # Default length
length_entry.pack()
length_entry.bind("<KeyRelease>", interval_length_changed)


# Create a button
button = ttk.Button(root, text="Graphen anzeigen", command=show_graphs)
button.pack()

# Footer frame
footer_frame = ttk.Frame(root)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Save settings button
save_button = ttk.Button(footer_frame, text="Einstellungen speichern", command=save_settings)
save_button.pack(side=tk.LEFT, padx=2, pady=5, fill=tk.X, expand=True)

# Impressum button
impressum_button = ttk.Button(footer_frame, text="Impressum", command=open_impressum_window)
impressum_button.pack(side=tk.LEFT, padx=(5, 2), pady=5, fill=tk.X, expand=True)

# Load settings button
load_button = ttk.Button(footer_frame, text="Einstellungen abrufen", command=load_settings)
load_button.pack(side=tk.LEFT, padx=2, pady=5, fill=tk.X, expand=True)


# Run the Tkinter event loop
root.mainloop()
