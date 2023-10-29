# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 07:26:30 2020

@author: RogelioTESI
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
params = {'xtick.labelsize': 20, 'ytick.labelsize': 20}
mpl.rcParams.update(params)
datos1=np.loadtxt("Frec1.csv",usecols=(0,1,2,),skiprows=1,delimiter=',')
datos2=np.loadtxt("Frec2.csv",usecols=(0,1,2,),skiprows=1,delimiter=',')
freq1=(datos1[:,0]);
am1=1e3*(datos1[:,1]);
am2=1e3*(datos1[:,2]);
freq2=(datos2[:,0]);
am3=1e3*(datos2[:,2]);
fig,axes=plt.subplots(figsize=(11, 6))
axes.scatter(freq1[746],am1[746], 80, color='red')
plt.annotate('596.86kHz, 14.142mA',
            xy=(freq1[746], am1[746]), xycoords='data',
            xytext=(-180, -70), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", color='red',linewidth=3,connectionstyle="arc3,rad=.01"))
axes.semilogx(freq1,am1, linewidth=3)
axes.set_ylabel('Current, $i_{out}$ (mA)',fontsize=22)
axes.set_xlabel('Frequency ($Hz$)',fontsize=22)
axes.grid(True)
plt.savefig('AnchoBanda.eps',dpi=1000,bbox_inches='tight')
