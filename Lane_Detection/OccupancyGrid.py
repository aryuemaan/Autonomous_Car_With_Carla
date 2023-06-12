#Source == Carla Simulation https://github.com/carla-simulator/carla
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from PIL import Image

def preprocess_image(image_path):
    # Read the image and convert it to grayscale
    image = Image.open(image_path).convert('L')
    
    # Threshold the image to obtain a binary occupancy map
    threshold = 128
    binary_map = np.array(image) > threshold
    
    return binary_map

def inverse_scanner(num_rows, num_cols, x, y, theta, meas_phi, meas_r, rmax, alpha, beta):
    m = np.zeros((num_rows, num_cols))
    for i in range(num_rows):
        for j in range(num_cols):
            # Find range and bearing relative to the input state (x, y, theta).
            r = math.sqrt((i - x)**2 + (j - y)**2)
            phi = (math.atan2(j - y, i - x) - theta + math.pi) % (2 * math.pi) - math.pi
            
            # Find the range measurement associated with the relative bearing.
            k = np.argmin(np.abs(np.subtract(phi, meas_phi)))
            
            # If the range is greater than the maximum sensor range, or behind our range
            # measurement, or is outside of the field of view of the sensor, then no
            # new information is available.
            if (r > min(rmax, meas_r[k] + alpha / 2.0)) or (abs(phi - meas_phi[k]) > beta / 2.0):
                m[i, j] = 0.5
            
            # If the range measurement lied within this cell, it is likely to be an object.
            elif (meas_r[k] < rmax) and (abs(r - meas_r[k]) < alpha / 2.0):
                m[i, j] = 0.7
            
            # If the cell is in front of the range measurement, it is likely to be empty.
            elif r < meas_r[k]:
                m[i, j] = 0.3
                
    return m

# Simulation time initialization.
T_MAX = 150
time_steps = np.arange(T_MAX)

# Initializing the robot's location.
x_0 = [30, 30, 0]

# The sequence of robot motions.
u = np.array([[3, 0, -3, 0], [0, 3, 0, -3]])
u_i = 1

# Robot sensor rotation command
w = np.multiply(0.3, np.ones(len(time_steps)))

# Parameters for the sensor model.
meas_phi = np.arange(-0.4, 0.4, 0.05)
rmax = 30 # Max beam range.
alpha = 1 # Width of an obstacle (distance about measurement to fill in).
beta = 0.05 # Angular width of a beam.

# Initialize the vector of states for our simulation.
x = np.zeros((3, len(time_steps)))
x[:, 0] = x_0

# Preprocess the input image to obtain a binary occupancy map
image_path = r'C:\Users\aryuemaan\Downloads\photo_2023-05-19_14-50-42.jpg'  # Replace with the path to your input image
true_map = preprocess_image(image_path)

# Get the dimensions of the map
M, N = true_map.shape

# Initialize the belief map.
# Assuming a uniform prior.
m = np.multiply(0.5, np.ones((M, N)))

# Initialize the log odds ratio.
L0 = np.log(np.divide(m, np.subtract(1, m)))

# Main simulation loop.
for t in range(1, len(time_steps)):
    # Update the robot's pose based on the motion model.
    x_i = x[0, t-1]
    y_i = x[1, t-1]
    theta_i = x[2, t-1]
    x[0, t] = x_i + u[0, u_i]
    x[1, t] = y_i + u[1, u_i]
    x[2, t] = theta_i + w[t]
    
    # Generate range measurements.
    ranges = inverse_scanner(M, N, x[0, t], x[1, t], x[2, t], meas_phi, np.arange(0, rmax, 0.1), rmax, alpha, beta)
    
    # Update the belief map.
    L = np.log(np.divide(np.subtract(1, ranges), ranges)) + L0
    m = np.divide(1, np.add(1, np.exp(L)))
    
    # Update the log odds ratio.
    L0 = L
    
# Plot the final map.
plt.imshow(m, cmap='gray', origin='lower')
plt.show()
