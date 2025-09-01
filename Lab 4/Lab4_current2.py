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
        if len(parts) == 6:
            x_axis.append(float(parts[0]))
            v_gen1.append(float(parts[3])/1000 + 0.000161)


t = np.linspace(0,0.05,2001)


funk3 = (-1/304)*np.exp((-3800/13)*t) + (1/304) #Step Response
funk4 = (1/304)*np.exp((-3800/13)*t) # Natural Response



plt.figure(dpi = 300)
plt.plot(x_axis,v_gen1, label='Measured $i_{2}(t)$',color='black',linestyle='-')
plt.grid()
plt.title("ECE2260 - Lab 4 - $i_{2}(t)$")
plt.plot(t, funk3, color='red',linestyle='--', label='Calculated $i_{2}(t)$')
plt.plot(t-0.05, funk4, color='red',linestyle='--')
plt.xlabel("Time {s}")
plt.ylabel("Current {A}")
plt.legend()
plt.savefig('current2.png')
plt.show()