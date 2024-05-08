import math
import numpy as np
import matplotlib.pyplot as plt

# Konstanten
g = 9.81  # Erdbeschleunigung in m/s^2
M = 0.02896  # mittlere molare Masse der Luft in kg/mol
R = 8.314  # allgemeine Gaskonstante in J/(mol*K)
T0 = 288.15  # Temperatur auf Meereshöhe in Kelvin
rho0 = 1.225  # Luftdichte auf Meereshöhe in kg/m^3

# Benutzereingaben oder Standardwerte
A = float(input("Gib die Frontfläche der Rakete in m^2 ein (Standardwert ist 10): ") or 10)
cw = float(input("Gib den Strömungswiderstandsbeiwert ein (Standardwert ist 0.3): ") or 0.3)
v = float(input("Gib die Geschwindigkeit der Rakete relativ zur Luft in m/s ein (Standardwert ist 100): ") or 100)
startzeit = float(input("Gib die Startzeit in Sekunden ein (Standardwert ist 0): ") or 0)
endzeit = float(input("Gib die Endzeit in Sekunden ein (Standardwert ist 120): ") or 120)
schrittweite = float(input("Gib die Schrittweite für die Zeit in Sekunden ein (Standardwert ist 1): ") or 1)

def luftdichte(h):
    T = T0 - 0.0065 * h  # Temperatur in Kelvin
    rho = rho0 * math.exp(-g * M * h / (R * T))
    return rho


def luftwiderstand(h):
    rho = luftdichte(h)
    FL = 0.5 * cw * rho * A * v ** 2
    return FL

# Zeitpunkte für die Berechnung des Luftwiderstands
zeiten = np.arange(startzeit, endzeit + schrittweite, schrittweite)

# Luftwiderstand für jeden Zeitpunkt berechnen
luftwiderstand_werte = [luftwiderstand(h) for h in zeiten]

# Diagramm erstellen
plt.figure(figsize=(10, 6))
plt.plot(zeiten, luftwiderstand_werte, color='b', linestyle='-')
plt.title('Luftwiderstand während des Raketenstarts')
plt.xlabel('Zeit (s)')
plt.ylabel('Luftwiderstand (N)')
plt.grid(True)
plt.show()