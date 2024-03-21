import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bright_stars.csv')

df_filtered = df[df['Distance'] <= 100]

df_filtered = df_filtered[(df_filtered['gravity'] >= 150) & (df_filtered['gravity'] <= 350)]

df_filtered.to_csv('filtered_stars.csv', index=False)
