import numpy as np
import matplotlib.pyplot as plt
import customtkinter
from tkinter import messagebox

diagram = 8 # 0 = s(t) # 1 = v(t) # 2 = a(t) # 21 = s(t) + v(t) # 20 = a(t) + s(t) # 10 = v(t) + s(t) # 210 = s(t) + v(t) + a(t) # 8 = default (start damit nichts passiert)
'''
Tmax = 5
dt = 0.05
v0 = 2
rho = 1.29
A = 0.00126
cw = 0.45
m = 0.0027
g = 9.81
'''
def plot(x_values, y_values):
    plt.plot(x_values, y_values, marker="o") #Diagramm erstellen
    plt.xlabel("Folgenglied")
    plt.ylabel("Wert")
    plt.title("Diagramm der Folge")
    plt.grid(True)


def button():
    Tmax = input_tmax.get().replace(",", ".")
    dt = input_dt.get().replace(",", ".")
    v0 = input_v0.get().replace(",", ".")
    rho = input_rho.get().replace(",", ".")
    A = input_A.get().replace(",", ".")
    cw = input_cw.get().replace(",", ".")
    m = input_m.get().replace(",", ".")
    g = input_g.get().replace(",", ".")

    try:
        Tmax = float(Tmax)
    except ValueError:
        messagebox.showerror("Fehler", "Die Dauer muss eine Zahl sein.")
        return
    try:
        dt = float(dt)
    except ValueError:
        messagebox.showerror("Fehler", "Der Intervall muss eine Zahl sein.")
        return
    if Tmax < dt:
        messagebox.showerror("Fehler", "Der Intervall muss kleiner sein als die Gesamtdauer.")
        return
    try:
        v0 = float(v0)
    except ValueError:
        messagebox.showerror("Fehler", "Die Anfangsgeschwindigkeit muss eine Zahl sein.")
        return
    try:
        rho = float(rho)
    except ValueError:
        messagebox.showerror("Fehler", "Die Dichte muss eine Zahl sein.")
        return
    try:
        A = float(A)
    except ValueError:
        messagebox.showerror("Fehler", "Die Querschnittsfläche muss eine Zahl sein.")
        return
    try:
        cw = float(cw)
    except ValueError:
        messagebox.showerror("Fehler", "Die Windschnittigkeit muss eine Zahl sein.")
        return
    try:
        m = float(m)
    except ValueError:
        messagebox.showerror("Fehler", "Die Masse muss eine Zahl sein.")
        return
    try:
        g = float(g)
    except ValueError:
        messagebox.showerror("Fehler", "Die Gravitation muss eine Zahl sein.")
        return

    #diagram richtige Zahl
    if s_var.get() == "on" and v_var.get() == "off" and a_var.get() == "off":
        diagram = 0
    elif s_var.get() == "off" and v_var.get() == "on" and a_var.get() == "off":
        diagram = 1
    elif s_var.get() == "off" and v_var.get() == "off" and a_var.get() == "on":
        diagram = 2
    elif s_var.get() == "off" and v_var.get() == "on" and a_var.get() == "on":
        diagram = 21
    elif s_var.get() == "on" and v_var.get() == "off" and a_var.get() == "on":
        diagram = 20
    elif s_var.get() == "on" and v_var.get() == "on" and a_var.get() == "off":
        diagram = 10
    elif s_var.get() == "on" and v_var.get() == "on" and a_var.get() == "on":
        diagram = 210
    elif s_var.get() == "off" and v_var.get() == "off" and a_var.get() == "off":
        diagram = 3 # Keine Diagramme ausgewählt

    time = np.zeros(int(Tmax / dt))
    velocity = np.zeros(int(Tmax / dt))
    acc = np.zeros(int(Tmax / dt))
    dist = np.zeros(int(Tmax / dt))

    velocity[0] = v0
    dist[0] = 0

    for x in range(time.size - 1):
        # jedes Intervall ist dt lang
        time[x + 1] = time[x] + dt

        # Die aktuelle Acceleration/Beschleunigung berechnen
        acc[x] = g - 0.5 * (cw * rho * A) / m * pow(velocity[x], 2)
        # Die Steigerung der Geschwidnigkeit berechnen
        incV = acc[x] * dt
        # Zur aktuellen Geschwindigkeit die Graphen berechnen
        velocity[x + 1] = velocity[x] + incV

        dist[x + 1] = dist[x] + velocity[x] * dt
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
    elif diagram == 8:
        pass
    elif diagram == 3:
        messagebox.showerror("Fehler", "Keine Diagramme wurden ausgewählt.")
    else:
        messagebox.showerror("Fehler", "Es liegt ein Fehler vor. Das muss an Ihnen legen.")
    plt.show()

def switch_event():
    pass


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x660")
app.resizable(False, False)
app.title("Freier Fall Berechnung mit Luftwiderstand")

input_tmax = customtkinter.CTkEntry(app, width=300, placeholder_text="Dauer in s")
input_tmax.place(relx=0.5, rely=0.05, anchor=customtkinter.CENTER)

input_dt = customtkinter.CTkEntry(app, width=300, placeholder_text="Intervall in s")
input_dt.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)

input_v0 = customtkinter.CTkEntry(app, width=300, placeholder_text="Anfangsgeschwindigkeit in m/s")
input_v0.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

input_rho = customtkinter.CTkEntry(app, width=300, placeholder_text="Dichte der Luft")
input_rho.place(relx=0.5, rely=0.35, anchor=customtkinter.CENTER)

input_A = customtkinter.CTkEntry(app, width=300, placeholder_text="Querschnittsfläche")
input_A.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)

input_cw = customtkinter.CTkEntry(app, width=300, placeholder_text="Windschnittigkeit")
input_cw.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

input_m = customtkinter.CTkEntry(app, width=300, placeholder_text="Masse")
input_m.place(relx=0.5, rely=0.65, anchor=customtkinter.CENTER)

input_g = customtkinter.CTkEntry(app, width=300, placeholder_text="Gravitation")
input_g.insert(0, "9.81")
input_g.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

s_var = customtkinter.StringVar(value="on")
s_switch = customtkinter.CTkSwitch(app, text="s(t)", command=switch_event, variable=s_var, onvalue="on", offvalue="off")
s_switch.place(relx=0.3, rely=0.85, anchor=customtkinter.CENTER)

v_var = customtkinter.StringVar(value="off")
v_switch = customtkinter.CTkSwitch(app, text="v(t)", command=switch_event, variable=v_var, onvalue="on", offvalue="off")
v_switch.place(relx=0.5, rely=0.85, anchor=customtkinter.CENTER)

a_var = customtkinter.StringVar(value="off")
a_switch = customtkinter.CTkSwitch(app, text="a(t)", command=switch_event, variable=a_var, onvalue="on", offvalue="off")
a_switch.place(relx=0.7, rely=0.85, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, width=300, text="Berechnen", command=button)
button.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

app.mainloop()