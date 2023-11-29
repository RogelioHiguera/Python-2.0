# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:39:23 2023

@author: Rogelio Higuera
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
t = np.linspace(0, 1, 1000, False)  # 1 second
Tm = t[10]-t[9]
fs1 = 1/Tm
sig = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(t, sig)
ax1.set_title('10 Hz and 20 Hz sinusoids')
ax1.axis([0, 1, -2, 2])
sos = signal.butter(10, [1,15], 'bp', fs=fs1, output='sos')
filtered = signal.sosfilt(sos, sig)
ax2.plot(t, filtered)
ax2.set_title('After 15 Hz high-pass filter')
ax2.axis([0, 1, -2, 2])
ax2.set_xlabel('Time [seconds]')
plt.tight_layout()
plt.show()