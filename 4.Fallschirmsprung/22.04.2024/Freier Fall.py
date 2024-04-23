import numpy as np
import matplotlib.pyplot as plt
import customtkinter
from tkinter import messagebox

diagram = 0 # 0 = s(t) # 1 = v(t) # 2 = a(t) # 21 = s(t) + v(t) # 20 = a(t) + s(t) # 10 = v(t) + s(t) # 210 = s(t) + v(t) + a(t)

Tmax = 5
dt = 0.05
v0 = 2
rho = 1.29
A = 0.00126
cw = 0.45
m = 0.0027
g = 9.81

time = np.zeros(int(Tmax/dt))
velocity = np.zeros(int(Tmax/dt))
acc = np.zeros(int(Tmax/dt))
dist = np.zeros(int(Tmax/dt))

velocity[0] = v0
dist[0] = 0

for x in range(time.size-1):
    #jedes Intervall ist dt lang
    time[x+1] = time[x] + dt


    #Die aktuelle Acceleration/Beschleunigung berechnen
    acc[x] = g - 0.5 * (cw * rho * A)/m * pow(velocity[x],2)
    #Die Steigerung der Geschwidnigkeit berechnen
    incV = acc[x] * dt
    #Zur aktuellen Geschwindigkeit die Graphen berechnen
    velocity[x+1] = velocity[x] + incV

    dist[x+1] = dist[x] + velocity[x] * dt

def plot(x_values, y_values):
    plt.plot(x_values, y_values, marker="o") #Diagramm erstellen
    plt.xlabel("Folgenglied")
    plt.ylabel("Wert")
    plt.title("Diagramm der Folge")
    plt.grid(True)
    #plt.show()

def button(diagram):
    # 0 = s(t) # 1 = v(t) # 2 = a(t) # 21 = s(t) + v(t) # 20 = a(t) + s(t) # 10 = v(t) + s(t) # 210 = s(t) + v(t) + a(t)
    if diagram == 0:
        plot(time, dist) # s(t)
    elif diagram == 1:
        plot(time, velocity) # v(t)
    elif diagram == 2:
        plot(time, acc) # a(t)
    elif diagram == 21:
        plot(time, velocity) # v(t)
        plot(time, acc)  # a(t)
    elif diagram == 20:
        plot(time, dist) # s(t)
        plot(time, acc)  # a(t)
    elif diagram == 10:
        plot(time, dist) # s(t)
        plot(time, velocity)  # v(t)
    elif diagram == 210:
        plot(time, dist) # s(t)
        plot(time, velocity)  # v(t)
        plot(time, acc)  # a(t)
    else:
        messagebox.showerror("Fehler", "Es liegt ein Fehler vor. Das muss an Ihnen legen.")
    plt.show()

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x400")
app.title("Freier Fall Berechnung mit Luftwiderstand")

anzahlkerne = customtkinter.CTkEntry(app, width=300, placeholder_text="Anzahl Atomkerne")
anzahlkerne.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)
prob = customtkinter.CTkEntry(app, width=300, placeholder_text="Zerfallswahrscheinlichkeit")
prob.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=app, width=300, text="Berechnen", command=button(diagram))
button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

app.mainloop()