import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bright_stars.csv')

if 'gravity' not in df.columns:
    raise ValueError("Gravity data not found in the dataframe.")

mass_data = df['Mass'].tolist()
radius_data = df['Radius'].tolist()
gravity_data = df['gravity'].tolist()

mass_data.sort()
radius_data.sort()
gravity_data.sort()

# plot for mass vs radius
plt.figure(figsize=(10, 6))
plt.plot(mass_data, radius_data, marker='o', linestyle='-', color='b')
plt.title('Mass vs Radius of Stars')
plt.xlabel('Mass (Solar Mass)')
plt.ylabel('Radius (Solar Radius)')
plt.grid(True)
plt.show()

# plot for mass vs gravity
plt.figure(figsize=(10, 6))
plt.plot(mass_data, gravity_data, marker='o', linestyle='-', color='r')
plt.title('Mass vs Gravity of Stars')
plt.xlabel('Mass (Solar Mass)')
plt.ylabel('Gravity (m/s^2)')
plt.grid(True)
plt.show()
