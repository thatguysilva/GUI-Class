import math

# Prompt the user for initial velocity and angle
v0 = float(input("Enter the initial velocity in meters per second: "))
theta = float(input("Enter the angle in degrees: "))

# Convert the angle to radians
theta = math.radians(theta)

# Calculate the maximum reach of the projectile
g = 9.81  # gravitational acceleration in meters per second squared
R = (v0 ** 2 * math.sin(2 * theta)) / g

# Print the result
print(f"The maximum reach of the projectile is {R:.2f} meters.")
