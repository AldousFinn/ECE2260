import csv
import matplotlib.pyplot as plt
import numpy as np


x_axis = []
v_gen1 = []


with open('scope_6.csv',newline='') as csvfile:
    for i,line in enumerate(csvfile):
        if i<3:
            continue
        parts = line.strip().split(',')
        if len(parts) == 2:
            x_axis.append(float(parts[0]))
            v_gen1.append(float(parts[1]))
            


t = np.linspace(0,3.23e-3,677)
s = np.linspace(0, 3.23e-3, 677)


funk3 = 5 - 8.501*np.exp(-6417.42*t) + 3.501*np.exp(-15582.58*t)
funk4 = 8.5*np.exp(-6417.42*t) - 3.5*np.exp(-15582.58*t)




plt.figure()
plt.plot(x_axis,v_gen1, label='Measured $i(t)$',color='black',linestyle='-')
plt.grid()

plt.plot(t, funk3 + 2.5, label = 'Theoretical $V_{C}$(t)', color='red',linestyle='--')
plt.plot(s - 0.00331, funk4 + 2.5, color='red',linestyle='--')

plt.legend()
plt.show()