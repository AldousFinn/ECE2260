import csv
import matplotlib.pyplot as plt
import numpy as np


x_axis = []
v_gen1 = []


with open('scope_5.csv',newline='') as csvfile:
    for i,line in enumerate(csvfile):
        if i<3:
            continue
        parts = line.strip().split(',')
        if len(parts) == 2:
            x_axis.append(float(parts[0]) + 0.00345)
            v_gen1.append(float(parts[1])/2250)


t = np.linspace(0,3.23e-3,677)
s = np.linspace(0, 3.23e-3, 677)


funk3 = -(6.1894*np.exp(-6417.42*t)-0.98505*np.exp(-15582.58*t))/(1801+399)
funk4 = (6.1894*np.exp(-6417.42*s)-0.98505*np.exp(-15582.58*s))/(1801+399)




plt.figure()
plt.plot(x_axis,v_gen1, label='Measured $i(t)$',color='black',linestyle='-')
plt.grid()

plt.plot(t + 0.00012, funk3 + 0.00005, color='red',linestyle='--')
plt.plot(s + 0.0035, funk4, label = 'Theoretical $i(t)$', color='red',linestyle='--')

plt.legend()
plt.show()

#9.83346*np.exp(-6417.42*t) - 9.83346*np.exp(-15582.58*t) V
#L*di/dt = -8.84841*np.exp(-15582.58*t)-3.6441*np.exp(-6417.42*t)
#Vtotal = 6.1894*np.exp(-6417.42*t)-0.98505*np.exp(-15582.58*t)