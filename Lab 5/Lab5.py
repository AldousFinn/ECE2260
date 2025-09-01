import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cont2discrete, dimpulse, lfilter, sawtooth


x_axis = []
v_gen1 = []


with open('scope_2.csv',newline='') as csvfile:
    for i,line in enumerate(csvfile):
        if i<3:
            continue
        parts = line.strip().split(',')
        if len(parts) == 4:
            x_axis.append(float(parts[0]) + 0.005986)
            v_gen1.append(float(parts[2]) + 1.6)





num_ct = [20000*11, 20000*5000]
den_ct = [11, 445000, 100000000]

fs = 1000
Ts = 1 / fs

system_discrete = cont2discrete((num_ct, den_ct), Ts, method='zoh')
b_coeffs = system_discrete[0].flatten()
a_coeffs = system_discrete[1].flatten()
dt = system_discrete[2]

input_signal = np.zeros(100)

signal_length = 100
t = np.arange(signal_length) / fs
#input_signal[0:50] = 5
#input_signal[51:100] = 0

input_signal = 2.5 * (1 + sawtooth(2 * np.pi * 50 * t, width=0.5))

system = (b_coeffs, a_coeffs, dt)
time_steps, impulse_response_tuple = dimpulse(system, n = 100)
impulse_response = np.squeeze(impulse_response_tuple)

convolved_result = np.convolve(input_signal, impulse_response, mode = 'full')
conv_trimmed = convolved_result[:signal_length]

filtered_result = lfilter(b_coeffs, a_coeffs, input_signal)

plt.figure(figsize=(10, 6))


plt.title('Sawtooth Impulse Response')
plt.ylabel('Amplitude (V)')
plt.xlabel('Time (s)')
plt.grid(True)

#plt.plot(t, input_signal - 2.5, color = 'blue', label='Input Signal')
plt.plot(t, impulse_response, color = 'blue', label='Impulse Reponse')
plt.legend()

"""plt.subplot(2, 1, 1)
plt.plot(x_axis, v_gen1, label='Measured $V$', color='black', linewidth=1)
plt.plot(t, conv_trimmed - 0.8, label='Analytical Convolution', color='blue', linestyle='--')
plt.title('Measured vs Convolution Output [$H_{1}(s)$]')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend(loc="upper left")

plt.subplot(2, 1, 2)
plt.plot(x_axis, v_gen1, label='Measured $V$', color='black', linewidth=1)
plt.plot(t, filtered_result - 0.8, label='Analytical Filter', color='green', linestyle='--')
plt.title('Measured vs Filtered Output [$H_{1}(s)$]')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend(loc="upper left")

plt.tight_layout()"""
plt.show()