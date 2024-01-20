# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:20:56 2024

@author: alexa
"""

import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d

#This estimate is particularly relevant in cases where the grounding configuration involves cylindrical-shaped turbine foundations with multiple driven pillars, constructed of reinforced concrete, and horizontal electrodes.

#Enter with s(m)
s = input("Please enter the distance between grounding turbine and horizontal electrode (s) in meters: ")

# Dados fornecidos

data = {
    's (m)': [0.0001, 0.0003, 0.0005, 0.0008, 0.001, 0.003, 0.005, 0.01, 0.02, 0.03,
              0.04, 0.05, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.4, 20, 30, 40, 50, 60,
              70, 80, 100],

    'k': [4.34783E-07, 0.00879087, 0.014403261, 0.02251087, 0.02768913, 0.071967391, 0.105786957, 0.163593478, 0.225456522, 0.258565217,
          0.280847826, 0.295326087, 0.44323913, 0.500673913, 0.5395, 0.569326087, 0.59373913, 0.614391304, 0.632282609, 0.648065217,
          0.662173913, 0.674891304, 0.690652174, 0.7585, 0.804608696, 0.834695652, 0.856130435, 0.872282609, 0.884913043, 0.895086957,
          0.910565217],
}

# Criando um DataFrame com os dados
df = pd.DataFrame(data)

interp_func = interp1d(df['s (m)'], df['k'], kind='linear', fill_value='extrapolate')
valor_interpolado = interp_func(s)

print(f"Interpolated value for a given s of {s} (m) is k: {valor_interpolado}.")

# Plotando os dados
plt.figure(figsize=(10, 6))
plt.grid(True)
plt.xscale('log')
plt.plot(df['s (m)'], df['k'], label='k')

plt.xlabel('s (m)')
plt.ylabel('k')
plt.title('Relationship between s and k')
plt.legend()

plt.show()

