import customtkinter
import matplotlib.pyplot as plt
from tkinter import messagebox
import numpy as np
##push
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
        num_atoms = int(anzahlkerne.get())
        decay_prob = float(prob.get().replace(',','.'))
        plot_decay(num_atoms, decay_prob)
    except ValueError:
        num_atoms = anzahlkerne.get()
        try:
            decay_prob = int(prob.get())
            decay_prob = prob.get()
        except:
            decay_prob = "a"
        if num_atoms.isdigit() == False:
            messagebox.showerror("Fehler", "Die Anzahl der Atomkerne muss eine gültige Zahl sein.")
        elif decay_prob.isdigit() == False:
            messagebox.showerror("Fehler", "Wahrscheinlichkeit muss zwischen 0 und 1 liegen und darf keine Buchstaben beinhalten.")
        else:
            messagebox.showerror("Fehler", "Es muss einen Fehler geben. Versuchen Sie es erneut.")

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x400")
app.title("M. Curie")

# Use CTkButton instead of tkinter Button
anzahlkerne = customtkinter.CTkEntry(app, width=300, placeholder_text="Anzahl Atomkerne")
anzahlkerne.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
prob = customtkinter.CTkEntry(app, width=300, placeholder_text="Zerfallswahrscheinlichkeit")
prob.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=app, width=300, text="Berechnen", command=start_simulation)
button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

app.mainloop()