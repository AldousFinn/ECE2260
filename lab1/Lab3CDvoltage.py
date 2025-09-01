import csv
import matplotlib.pyplot as plt
import numpy as np


x_axis = []
v_gen1 = []


with open('scope_8.csv',newline='') as csvfile:
    for i,line in enumerate(csvfile):
        if i<3:
            continue
        parts = line.strip().split(',')
        if len(parts) == 2:
            x_axis.append(float(parts[0]))
            v_gen1.append(float(parts[1]))


t = np.linspace(0,3.23e-3,677)
s = np.linspace(0, 3.32e-3, 677)


funk3 = 5 - 50000*t*np.exp(-10000*t) - 5*np.exp(-10000*t)
funk4 = 50000*t*np.exp(-10000*t) + 5*np.exp(-10000*t)




plt.figure()
plt.plot(x_axis,v_gen1, label='Measured $i(t)$',color='black',linestyle='-')
plt.grid()

plt.plot(t, funk3 + 2.4, color='red',linestyle='--')
plt.plot(s - 0.00338, funk4 + 2.4, label = 'Theoretical $i(t)$', color='red',linestyle='--')

plt.legend()
plt.show()