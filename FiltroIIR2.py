# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:23:14 2023
Filtro IIR Prueba 2
@author: Rogelio Manuel Higuera González 
Academia: Ingeniería Electrónica
"""
import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal 
from scipy.fftpack import fft, fftfreq 
import matplotlib as mpl
parameters = {'xtick.labelsize':13, 'ytick.labelsize':13}
mpl.rcParams.update(parameters)
"""
Lectura y gráfica de la señal de ECG
"""
Data = np.loadtxt('ECG2.csv', usecols=(0,1,),skiprows=1,delimiter=',')
Time = (Data[:,0])
Amplitude = (Data[:,1])
fig, axes = plt.subplots()
axes.plot(Time,Amplitude,linewidth=2)
axes.set_xlabel('Time [s]')
axes.set_ylabel('Amplitude [V]')
axes.grid(True)
"""
Sacar FFT de la señal 
"""
n = len(Time) #Número de datos
Tm = Time[10]-Time[9] #Periodo de muestreo
fs1 = 1/Tm #Frecuencia de muestreo
y1 = abs(fft(Amplitude/n))
frec1 = abs(fftfreq(n,Tm))
fig, axes1 = plt.subplots()
axes1.plot(frec1,y1,linewidth=2)
axes1.set_xlabel('Frequency [Hz]')
axes1.set_ylabel('Amplitude [V]')
axes1.grid(True)
"""
Filtro IIR Butterworth (respuesta en frecuencia)
"""
order = 10 #Orden del filtro 
fc1 = 0.1 #Frecuencia de corte 1
fc2 = 100 #Frecuencia de corte 2
wc1 = 2*np.pi*fc1 #Frecuencia angular 1
wc2 = 2*np.pi*fc2 #Frecuencia angular 2
rs1 = 60 #Proporciona la minima atenuación en la banda de rechazo (dB)
b,a = signal.iirfilter(order, [wc1,wc2], rs=rs1, btype='band', analog=True, ftype='butter')
w, h = signal.freqs(b, a, 1000)
fig, axes2 = plt.subplots()
axes2.semilogx(w/(2*np.pi),20*np.log10(np.maximum(abs(h),1e-5)),linewidth=2)
axes2.set_xlabel('Frecuencia [Hz]')
axes2.set_ylabel('Amplitud [dB]')
axes2.grid(True)
"""
Señal filtrada
"""
sos = signal.butter(order, [fc1,fc2], 'bp', fs=fs1, output='sos')
filtered = signal.sosfilt(sos, Amplitude)
fig, axes3 = plt.subplots()
axes3.plot(Time,filtered,linewidth=2)
axes3.set_xlabel('Time [s]')
axes3.set_ylabel('Amplitude [V]')
axes3.grid(True)
"""
fft de la señal filtrada
"""
y2 = abs(fft(filtered/n))
frec2 = abs(fftfreq(n,Tm))
fig, axes4 = plt.subplots()
axes4.plot(frec2,y2,linewidth=2)
axes4.set_xlabel('Frequency [Hz]')
axes4.set_ylabel('Amplitude [V]')
axes4.grid(True)