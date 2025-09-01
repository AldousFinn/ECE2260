import csv
import matplotlib.pyplot as plt
import numpy as np


x_axis = []
v_gen1 = []


with open('scope_2.csv',newline='') as csvfile:
    for i,line in enumerate(csvfile):
        if i<3:
            continue
        parts = line.strip().split(',')
        if len(parts) == 5:
            x_axis.append(float(parts[0]))
            v_gen1.append(float(parts[2])/470 - 0.000202)


t = np.linspace(0,0.05,2001)


funk3 = (25/3952)*np.exp((-3800/13)*t) + (1/304) #Step Response
funk4 = (-25/3952)*np.exp((-3800/13)*t) # Natural Response



plt.figure()
plt.plot(x_axis,v_gen1, label='Measured $i(t)$',color='black',linestyle='-')
plt.grid()

plt.plot(t, funk3, color='red',linestyle='--', label='Calculated $i(t)$')
plt.plot(t-0.05, funk4, color='red',linestyle='--')

plt.legend()
plt.show()