import csv
import matplotlib.pyplot as plt
import numpy as np


x_axis = []
v_gen1 = []


with open('scope_1.csv',newline='') as csvfile:
    for i,line in enumerate(csvfile):
        if i<3:
            continue
        parts = line.strip().split(',')
        if len(parts) == 4:
            x_axis.append(float(parts[0]))
            v_gen1.append(float(parts[2]))
            


t = np.linspace(0,3.23e-3,677)
s = np.linspace(0, 3.23e-3, 677)


funk3 = 5 - 5*np.exp(-2350*t)*np.cos(9719.95*t) - 1.21*np.exp(-2350*t)*np.sin(9719.95*t)
funk4 = 5*np.exp(-2350*s)*np.cos(9719.95*s) + 1.21*np.exp(-2350*s)*np.sin(9719.95*s)




plt.figure()
plt.plot(x_axis,v_gen1, label='Measured $i(t)$',color='black',linestyle='-')
plt.grid()

plt.plot(t, funk3 + 2.5, label = 'Theoretical $V_{C}$(t)', color='red',linestyle='--')
plt.plot(s - 0.00331, funk4 + 2.5, color='red',linestyle='--')

plt.legend()
plt.show()