import pandas as pd

df = pd.read_csv('bright_stars.csv')

star_names = df['Star_name'].tolist()
mass = df['Mass'].tolist()
radius = df['Radius'].tolist()
distance = df['Distance'].tolist()
gravity = df['gravity'].tolist()

star_data = []
for i in range(len(star_names)):
    star_data.append({
        'Star_name': star_names[i],
        'Mass': mass[i],
        'Radius': radius[i],
        'Distance': distance[i],
        'gravity': gravity[i]
    })

final_list = star_data.copy()


final_data = final_list

