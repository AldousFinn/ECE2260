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
            x_axis.append(float(parts[0]) + 0.00345)
            v_gen1.append(float(parts[1])/1966)


t = np.linspace(0,3.23e-3,677)
s = np.linspace(0, 3.23e-3, 677)


funk3 = ((26350*t +5.2)*np.exp(-10000*t))/1966
funk4 = -((26350*t +5.2)*np.exp(-10000*t))/1966




plt.figure()
plt.plot(x_axis,v_gen1, label='Measured $i(t)$',color='black',linestyle='-')
plt.grid()

plt.plot(t + 0.000181, funk3 + 0.00123, color='red',linestyle='--')
plt.plot(s + 0.00351, funk4 + 0.0038, label = 'Theoretical $i(t)$', color='red',linestyle='--')

plt.legend()
plt.show()

#Vr(t) = 78350*t*np.exp(-10000*t)
#L*di/dt = -52000(t-0.0001)*np.exp(-10000*t)
#Vtotal = (26350*t +5.2)*np.exp(-10000*t)