import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import csv
import numpy as np


x_axis = []
v_gen1 = []
phi_gen1 = []

with open('scope_1.csv',newline='') as csvfile:
    for i,line in enumerate(csvfile):
        if i<1:
            continue
        parts = line.strip().split(',')
        if len(parts) == 5:
            x_axis.append(float(parts[1])*2*(np.pi))
            v_gen1.append(float(parts[3]))
            phi_gen1.append(float(parts[4]))


R = 10000
C = 0.0103e-6
numerator_tf=[R*C, 0]
denominator_tf = [R*C,1]
frequencies_theory = np.logspace(1,10,1000)

system = signal.TransferFunction(numerator_tf,denominator_tf)
w_bode, mag_db_scipy, phase_deg_scipy = signal.bode(system,w=2*np.pi*frequencies_theory)

fig, axs = plt.subplots(2, 1, figsize=(8, 10))

axs[0].set_ylabel("Magnitude (dB)")
axs[0].set_title("ECE 2260 - Lab 6 - Magnitude Bode Plot")
axs[0].semilogx(w_bode, mag_db_scipy, color="red", linestyle='--', label='Theoretical Data')
axs[0].plot(x_axis, v_gen1, color='black', label='Measured Data')
axs[0].legend(['Theoretical Bode', 'Measured Data'])
axs[0].grid(True)
axs[0].set_xlim(10, 10e7)

axs[1].set_ylabel("Phase (degrees)")
axs[1].set_xlabel("Frequency (rad/s)")
axs[1].set_title("ECE 2260 - Lab 6 - Phase Bode Plot")
axs[1].semilogx(w_bode, phase_deg_scipy, color="red", linestyle='--', label='Theoretical Data')
axs[1].plot(x_axis, phi_gen1, color='black', label='Measured Data')
axs[1].legend(['Theoretical Data', 'Measured Data'])
axs[1].set_xlim(10, 10e7)
axs[1].grid(True)

plt.tight_layout()
plt.show()

