import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bright_stars.csv')

star_names = df['Star_name'].tolist()
mass = df['Mass'].tolist()
radius = df['Radius'].tolist()
distance = df['Distance'].tolist()
gravity = df['Gravity'].tolist()

# Plot bar charts
plt.figure(figsize=(12, 8))

# Star name vs Mass
plt.subplot(221)
plt.bar(star_names, mass, color='skyblue')
plt.title('Star Name vs Mass')
plt.xlabel('Star Name')
plt.ylabel('Mass (Solar Mass)')
plt.xticks(rotation=90)
plt.tight_layout()

# Star name vs Radius
plt.subplot(222)
plt.bar(star_names, radius, color='salmon')
plt.title('Star Name vs Radius')
plt.xlabel('Star Name')
plt.ylabel('Radius (Solar Radius)')
plt.xticks(rotation=90)
plt.tight_layout()

# Star name vs Distance
plt.subplot(223)
plt.bar(star_names, distance, color='lightgreen')
plt.title('Star Name vs Distance')
plt.xlabel('Star Name')
plt.ylabel('Distance (Light Years)')
plt.xticks(rotation=90)
plt.tight_layout()

# Star name vs Gravity
plt.subplot(224)
plt.bar(star_names, gravity, color='gold')
plt.title('Star Name vs Gravity')
plt.xlabel('Star Name')
plt.ylabel('Gravity (m/s^2)')
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
