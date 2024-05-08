import matplotlib.pyplot as plt
import math
import numpy as np


def simulate_rocket(initial_mass, gas_velocity, time_step, total_time):
    mass = initial_mass
    time_points = [0]
    masses = [initial_mass]

    current_time = 0
    while current_time < total_time:
        delta_mass = 0.1  # Change in mass for each time step (for demonstration)
        mass -= delta_mass
        current_time += time_step
        time_points.append(current_time)
        masses.append(mass)
        print(f"Time: {current_time} s, Mass: {mass} kg")

    return time_points, masses


def simulate_rocket_launch(duration, time_step, A=10, cw=0.3, v=100, startzeit=0, endzeit=120, schrittweite=1):
    time = [0]
    velocity = [0]
    acceleration = [0]
    distance = [0]

    for t in range(1, int(duration / time_step) + 1):
        time.append(t * time_step)
        acceleration.append(9.81)  # Beschleunigung durch Schwerkraft in m/s^2
        velocity.append(velocity[-1] + acceleration[-1] * time_step)
        distance.append(distance[-1] + velocity[-1] * time_step)

    # Luftwiderstand für jeden Zeitpunkt berechnen
    zeiten = np.arange(startzeit, endzeit + schrittweite, schrittweite)
    luftwiderstand_werte = [luftwiderstand(h, A, cw, v) for h in zeiten]

    return time, velocity, acceleration, distance, zeiten, luftwiderstand_werte


def luftdichte(h):
    g = 9.81  # Erdbeschleunigung in m/s^2
    M = 0.02896  # mittlere molare Masse der Luft in kg/mol
    R = 8.314  # allgemeine Gaskonstante in J/(mol*K)
    T0 = 288.15  # Temperatur auf Meereshöhe in Kelvin
    rho0 = 1.225  # Luftdichte auf Meereshöhe in kg/m^3

    T = T0 - 0.0065 * h  # Temperatur in Kelvin
    rho = rho0 * math.exp(-g * M * h / (R * T))
    return rho


def luftwiderstand(h, A, cw, v):
    rho = luftdichte(h)
    FL = 0.5 * cw * rho * A * v ** 2
    return FL


def plot_all(initial_mass, gas_velocity, time_step, total_time, duration, time_step_rl, A, cw, v, startzeit, endzeit,
             schrittweite):
    # Simulate rocket
    time_points, masses = simulate_rocket(initial_mass, gas_velocity, time_step, total_time)

    # simulate rocket launch
    time, velocity, acceleration, distance, zeiten, luftwiderstand_werte = simulate_rocket_launch(duration,
                                                                                                  time_step_rl, A, cw,
                                                                                                  v, startzeit, endzeit,
                                                                                                  schrittweite)

    # Plotting
    fig, axs = plt.subplots(3, 2, figsize=(14, 15))

    axs[0, 0].plot(time_points, masses, 'b-')
    axs[0, 0].set_title('Rocket Mass Over Time')
    axs[0, 0].set_xlabel('Time (s)')
    axs[0, 0].set_ylabel('Mass (kg)')

    axs[0, 1].plot(time, velocity, 'r-')
    axs[0, 1].set_title('Velocity during Rocket Launch')
    axs[0, 1].set_xlabel('Time (s)')
    axs[0, 1].set_ylabel('Velocity (m/s)')

    axs[1, 0].plot(time, acceleration, 'g-')
    axs[1, 0].set_title('Acceleration during Rocket Launch')
    axs[1, 0].set_xlabel('Time (s)')
    axs[1, 0].set_ylabel('Acceleration (m/s^2)')

    axs[1, 1].plot(time, distance, 'y-')
    axs[1, 1].set_title('Distance Travelled during Rocket Launch')
    axs[1, 1].set_xlabel('Time (s)')
    axs[1, 1].set_ylabel('Distance (m)')

    axs[2, 0].plot(zeiten, luftwiderstand_werte, color='b', linestyle='-')
    axs[2, 0].set_title('Air Resistance during Rocket Launch')
    axs[2, 0].set_xlabel('Time (s)')
    axs[2, 0].set_ylabel('Air Resistance (N)')

    axs[2, 1].axis('off')  # Disable the display of the empty plot in the third row and second column

    plt.tight_layout()
    plt.show()


# Inputs
initial_mass = 1000  # Initial mass of the rocket in kg
gas_velocity = 1000  # Velocity of gas relative to the rocket in m/s
time_step = 1  # Time step for simulation in seconds
total_time = 100  # Total time for simulation in seconds

duration = 100  # Standard-Dauer des Raketenstarts in Sekunden
time_step_rl = 1  # Standard-Zeitintervall in Sekunden
A = 10  # Standardwert für die Frontfläche der Rakete in m^2
cw = 0.3  # Standardwert für den Strömungswiderstandsbeiwert
v = 100  # Standardwert für die Geschwindigkeit der Rakete relativ zur Luft in m/s
startzeit = 0  # Standardwert für die Startzeit in Sekunden
endzeit = 120  # Standardwert für die Endzeit in Sekunden
schrittweite = 1  # Standardwert für die Schrittweite für die Zeit in Sekunden

# Benutzereingaben
initial_mass = float(
    input(f"Gib die Anfangsmasse der Rakete in kg ein (Standardwert ist {initial_mass}): ") or initial_mass)
gas_velocity = float(input(
    f"Gib die Gasgeschwindigkeit relativ zur Rakete in m/s ein (Standardwert ist {gas_velocity}): ") or gas_velocity)
total_time = float(
    input(f"Gib die Gesamtzeit der Simulation in Sekunden ein (Standardwert ist {total_time}): ") or total_time)

duration = float(input(f"Bitte geben Sie die Dauer des Raketenstarts in Sekunden ein (Standard ist {duration}): ") or duration)
time_step_rl = float(input(f"Bitte geben Sie das Zeitintervall in Sekunden ein (Standard ist {time_step_rl}): ") or time_step_rl)
A = float(input(f"Gib die Frontfläche der Rakete in m^2 ein (Standardwert ist {A}): ") or A)
cw = float(input(f"Gib den Strömungswiderstandsbeiwert ein (Standardwert ist {cw}): ") or cw)
v = float(input(f"Gib die Geschwindigkeit der Rakete relativ zur Luft in m/s ein (Standardwert ist {v}): ") or v)
startzeit = float(input(f"Gib die Startzeit in Sekunden ein (Standardwert ist {startzeit}): ") or startzeit)
endzeit = float(input(f"Gib die Endzeit in Sekunden ein (Standardwert ist {endzeit}): ") or endzeit)
schrittweite = float(
    input(f"Gib die Schrittweite für die Zeit in Sekunden ein (Standardwert ist {schrittweite}): ") or schrittweite)

plot_all(initial_mass, gas_velocity, time_step, total_time, duration, time_step_rl, A, cw, v, startzeit, endzeit,
         schrittweite)
