import csv
import matplotlib.pyplot as plt
import numpy as np


x_axis = []
v_gen1 = []


with open('scope_0.csv',newline='') as csvfile:
    for i,line in enumerate(csvfile):
        if i<3:
            continue
        parts = line.strip().split(',')
        if len(parts) == 2:
            x_axis.append(float(parts[0]) + 0.00345)
            v_gen1.append(float(parts[1])/420)


t = np.linspace(0,3.23e-3,677)
s = np.linspace(0, 3.23e-3, 677)


funk3 = -0.0119*np.exp(-2350*t)*(np.cos(9719.95*t)-0.21914*np.sin(9719.95*t))
funk4 = 0.0119*np.exp(-2350*s)*(np.cos(9719.95*s)-0.21914*np.sin(9719.95*s))




plt.figure()
plt.plot(x_axis,v_gen1, label='Measured $i(t)$',color='black',linestyle='-')
plt.grid()

plt.plot(t + 0.000181, funk3 - 0.0003, color='red',linestyle='--')
plt.plot(s + 0.00351, funk4 + 0.00015, label = 'Theoretical $i(t)$', color='red',linestyle='--')

plt.legend()
plt.show()