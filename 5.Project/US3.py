import matplotlib.pyplot as plt

def simulate_rocket_launch(duration, time_step):
    time = [0]
    velocity = [0]
    acceleration = [0]
    distance = [0]

    for t in range(1, int(duration / time_step) + 1):
        time.append(t * time_step)
        acceleration.append(9.81)  # Beschleunigung durch Schwerkraft in m/s^2
        velocity.append(velocity[-1] + acceleration[-1] * time_step)
        distance.append(distance[-1] + velocity[-1] * time_step)

    return time, velocity, acceleration, distance

def plot_rocket_launch(time, velocity, acceleration, distance):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))

    axs[0].plot(time, velocity, 'b-')
    axs[0].set_title('Geschwindigkeit während des Raketenstarts')
    axs[0].set_xlabel('Zeit (s)')
    axs[0].set_ylabel('Geschwindigkeit (m/s)')

    axs[1].plot(time, acceleration, 'r-')
    axs[1].set_title('Beschleunigung während des Raketenstarts')
    axs[1].set_xlabel('Zeit (s)')
    axs[1].set_ylabel('Beschleunigung (m/s^2)')

    axs[2].plot(time, distance, 'g-')
    axs[2].set_title('Zurückgelegte Strecke während des Raketenstarts')
    axs[2].set_xlabel('Zeit (s)')
    axs[2].set_ylabel('Zurückgelegte Strecke (m)')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    default_duration = 100  # Standard-Dauer des Raketenstarts in Sekunden
    default_time_step = 1  # Standard-Zeitintervall in Sekunden

    duration_input = input(f"Bitte geben Sie die Dauer des Raketenstarts in Sekunden ein (Standard ist {default_duration}): ")
    time_step_input = input(f"Bitte geben Sie das Zeitintervall in Sekunden ein (Standard ist {default_time_step}): ")

    duration = int(duration_input) if duration_input else default_duration
    time_step = int(time_step_input) if time_step_input else default_time_step

    time, velocity, acceleration, distance = simulate_rocket_launch(duration, time_step)
    plot_rocket_launch(time, velocity, acceleration, distance)
