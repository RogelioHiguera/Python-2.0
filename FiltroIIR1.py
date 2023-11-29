# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:42:44 2023
Filtro IIR Prueba 1
@author: Rogelio Manuel Higuera González 
Tecnológico Nacional de México
Academia: Ingeniería Electrónica
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy import signal 
n = 21 #Orden del filtro 
fc1 = 50 #Frecuencia de corte 1
fc2 = 100 #Frecuencia de corte 2
wc1 = 2*np.pi*fc1 #Frecuencia angular 1
wc2 = 2*np.pi*fc2 #Frecuencia angular 2
rs1 = 60 #Proporciona la minima atenuación en la banda de rechazo (dB)
b,a = signal.iirfilter(n, [wc1,wc2], rs=rs1, btype='band', analog=True, ftype='cheby2')
w, h = signal.freqs(b, a, 1000)
fig, axes = plt.subplots()
axes.semilogx(w/(2*np.pi),20*np.log10(np.maximum(abs(h),1e-5)),linewidth=2)
axes.set_xlabel('Frecuencia [Hz]')
axes.set_ylabel('Amplitud [dB]')
axes.grid(True)
