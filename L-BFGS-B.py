import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Load csv data
file_path = 'xy_data.csv'
data = pd.read_csv(file_path)

# Extract x, y values
x_data = data['x'].values
y_data = data['y'].values

# Generate t assuming uniform samples 6 to 60 matching data length
num_points = len(x_data)
t_data = np.linspace(6, 60, num_points)

# Parametric model function
# params = [theta_deg, M, X]
def model(params, t):
    theta_deg, M, X = params
    theta = np.radians(theta_deg)
    exp_term = np.exp(M * np.abs(t))
    x_pred = t * np.cos(theta) - exp_term * np.sin(0.3 * t) * np.sin(theta) + X
    y_pred = 42 + t * np.sin(theta) + exp_term * np.sin(0.3 * t) * np.cos(theta)
    return x_pred, y_pred

# Function to calculate point-wise and total L1 distances
def pointwise_l1_distance(params):
    x_pred, y_pred = model(params, t_data)
    l1_distances = np.abs(x_data - x_pred) + np.abs(y_data - y_pred)
    total_distance = np.sum(l1_distances)
    return l1_distances, total_distance

# Loss function for optimizer (only total L1)
def loss(params):
    _, total = pointwise_l1_distance(params)
    return total

# Bounds as given
bounds = [(0, 50), (-0.05, 0.05), (0, 100)]

# Initial guess (mid ranges)
initial_guess = [25, 0.0, 50]

# Optimize parameters to minimize total L1 loss
result = minimize(loss, initial_guess, bounds=bounds, method='L-BFGS-B')

# Extract optimized parameters and final loss
theta_opt, M_opt, X_opt = result.x
l1_values, total_l1 = pointwise_l1_distance(result.x)

print("Optimized Parameters:")
print(f"Theta (degrees): {theta_opt}")
print(f"M: {M_opt}")
print(f"X: {X_opt}")
print(f"Total L1 distance: {total_l1}")

print("\nL1 distance at each data point:")
print(l1_values)

# Plotting data and fitted curve
x_fit, y_fit = model(result.x, t_data)

plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'ro', label='Observed Data')
plt.plot(x_fit, y_fit, 'b-', label='Fitted Parametric Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data vs Fitted Curve')
plt.legend()
plt.show()