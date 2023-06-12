import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the simulation
car_speed = 30  # km/h
pedestrian_speed = 5  # km/h
time_step = 0.1  # seconds

# Initialize the positions of the car and pedestrian
car_x = 0
car_y = 0
pedestrian_x = 10
pedestrian_y = 0

# Create a list to store the positions of the car and pedestrian over time
car_positions = []
pedestrian_positions = []

# Loop over time
for i in range(100):
    # Update the positions of the car and pedestrian
    car_x += car_speed * time_step
    pedestrian_x += pedestrian_speed * time_step

    # Check if the car and pedestrian collide
    if car_x >= pedestrian_x:
        # The car hits the pedestrian
        print("Car hits pedestrian!")

        # Break out of the loop
        break

    # Add the positions of the car and pedestrian to the list
    car_positions.append((car_x, car_y))
    pedestrian_positions.append((pedestrian_x, pedestrian_y))

# Plot the positions of the car and pedestrian over time
plt.plot(car_positions, 'b-', label='Car')
plt.plot(pedestrian_positions, 'r-', label='Pedestrian')
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.legend()
plt.show()
