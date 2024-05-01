import matplotlib.pyplot as plt

class RocketSimulation:
    def __init__(self, initial_mass, gas_velocity, time_step, total_time):
        self.initial_mass = initial_mass
        self.mass = initial_mass
        self.gas_velocity = gas_velocity
        self.time_step = time_step
        self.total_time = total_time
        self.time_points = [0]
        self.masses = [initial_mass]

    def simulate(self):
        current_time = 0
        while current_time < self.total_time:
            delta_mass = 0.1  # Change in mass for each time step (for demonstration)
            self.mass -= delta_mass
            impulse_change = delta_mass * self.gas_velocity
            current_time += self.time_step
            self.time_points.append(current_time)
            self.masses.append(self.mass)
            print(f"Time: {current_time} s, Mass: {self.mass} kg, Impulse Change: {impulse_change} Ns")

    def plot_mass(self):
        plt.plot(self.time_points, self.masses)
        plt.title('Rocket Mass Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Mass (kg)')
        plt.grid(True)
        plt.show()

def main():
    initial_mass = 1000  # Initial mass of the rocket in kg
    gas_velocity = 1000  # Velocity of gas relative to the rocket in m/s
    time_step = 1  # Time step for simulation in seconds
    total_time = 100  # Total time for simulation in seconds

    simulation = RocketSimulation(initial_mass, gas_velocity, time_step, total_time)
    simulation.simulate()
    simulation.plot_mass()

if __name__ == "__main__":
    main()
