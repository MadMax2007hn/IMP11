import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np


def simulate_decay(num_atoms, decay_prob):
    time_steps = 100
    decay_counts = [num_atoms]
    for _ in range(1, time_steps):
        decayed = np.random.binomial(decay_counts[-1], decay_prob)
        decay_counts.append(decay_counts[-1] - decayed)
    return decay_counts


def plot_decay(num_atoms, decay_prob):
    decay_counts = simulate_decay(num_atoms, decay_prob)
    plt.plot(range(len(decay_counts)), decay_counts, marker='o', linestyle='-')
    plt.xlabel('Zeit')
    plt.ylabel('Anzahl der Atomkerne')
    plt.title('Radioaktiver Zerfall')
    plt.grid(True)
    plt.show()


def start_simulation():
    try:
        num_atoms = int(num_atoms_entry.get())
        decay_prob = float(decay_prob_entry.get())
        plot_decay(num_atoms, decay_prob)
    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie gültige Zahlen ein.")


# GUI erstellen
root = tk.Tk()
root.title("Radioaktiver Zerfall Simulation")

# Eingabefelder
tk.Label(root, text="Anzahl der Atomkerne:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
num_atoms_entry = tk.Entry(root)
num_atoms_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Zerfallswahrscheinlichkeit (0-1):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
decay_prob_entry = tk.Entry(root)
decay_prob_entry.grid(row=1, column=1, padx=5, pady=5)

# Button für Simulation starten
simulate_button = tk.Button(root, text="Simulation starten", command=start_simulation)
simulate_button.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()