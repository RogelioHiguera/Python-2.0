# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 08:56:09 2021

@author: RogelioTESI
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
params = {'xtick.labelsize': 14, 'ytick.labelsize': 14}
mpl.rcParams.update(params)
datos=np.loadtxt("phasenoise.csv",usecols=(0,1,),skiprows=1,delimiter=',') 
Frecuencia=(datos[:,0])                                                    
Gain=(datos[:,1])                                                  
fig,axes=plt.subplots(figsize=(11, 5))
axes.plot(Frecuencia, Gain, label='M=11', linewidth = 2)
axes.plot(Frecuencia, 8*Gain, label='M=12', linewidth = 2)
axes.set_xlabel('Time(s)',fontsize = 16)
axes.set_ylabel('Voltage(mV)',fontsize = 16)
axes.grid(True)
plt.legend(bbox_to_anchor=(1,0),loc='lower right',borderaxespad=0.1,fontsize=16)
plt.savefig('Grafica.eps',dpi=800,bbox_inches='tight')
