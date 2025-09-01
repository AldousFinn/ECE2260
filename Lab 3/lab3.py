import csv
import matplotlib.pyplot as plt
import numpy as np


x_axis = []
v_gen1 = []
v_gen2 = []
v_cap = []

with open('scope_1.csv',newline='') as csvfile:
    for i,line in enumerate(csvfile):
        if i<3:
            continue
        parts = line.strip().split(',')
        if len(parts) == 5:
            x_axis.append(float(parts[0]))
            v_gen1.append(float(parts[2]))
            #v_gen2.append(float(parts[2]))
            #v_cap.append(float(parts[3]))


t = np.linspace(0,3.23e-3,677)
s = np.linspace(0, 3.23e-3, 677)
#funk = np.zeros_like(t)

#time1 = t < 0.00338
#time2 = t >= 0.00338

#time3 = s >= 0.00338

#funk[time1] = -0.018144*np.exp(-2350*t[time1])*np.sin(9719.95*t[time1])
#funk[time3] = 0.005144*np.exp(-2350*s[time3])*np.sin(9719.95*s[time3])

#funk1 = -0.018144*np.exp(-2350*t)*np.sin(9719.95*t)
#funk2 = 0.017144*np.exp(-2350*s)*np.sin(9719.95*s)

funk3 = 5 - 5*np.exp(-2350*t)*np.cos(9719.95*t) - 1.21*np.exp(-2350*t)*np.sin(9719.95*t)
funk4 = 5*np.exp(-2350*s)*np.cos(9719.95*s) + 1.21*np.exp(-2350*s)*np.sin(9719.95*s)
#funk[t >= 50e-3] = 2.71 + 3.2 * np.exp(-426.3 * (t-0.05)[t >= 50e-3])
#funk[t >= 75e-3] = 2.71 * np.exp(-440.8 * (t-0.075)[t >= 75e-3])



plt.figure()
plt.plot(x_axis,v_gen1, label='Measured $i(t)$',color='black',linestyle='-')
plt.grid()
#plt.plot(t,funk1,label='Theoretical $i(t)$',color='red',linestyle='--')
#plt.plot(t + 0.00334,funk2,label='Theoretical $i(t)$',color='red',linestyle='--')
plt.plot(t, funk3 + 2.5, label = 'Theoretical $V_{C}$(t)', color='red',linestyle='--')
plt.plot(s - 0.00331, funk4 + 2.5, color='red',linestyle='--')
# plt.title('Charging and Discharging of Capacitor Voltage')
plt.legend()
plt.show()