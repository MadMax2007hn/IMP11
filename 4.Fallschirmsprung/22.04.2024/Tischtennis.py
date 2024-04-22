import numpy as np
import matplotlib.pyplot as plt

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

plot(time, velocity)
plot(time, dist)

plt.show()