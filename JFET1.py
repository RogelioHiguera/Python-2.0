# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:22:14 2022

@author: Rogelio Higuera
"""
import numpy as np
import matplotlib.pyplot as plt
IDSS = 6e-3
VP = -3.5
VGS = np.linspace(VP,0,num=100)
ID = IDSS*(1-(VGS/VP))**2
fig,axes=plt.subplots()
axes.plot(VGS,ID*1e3,linewidth=2)
axes.set_ylabel('Corriente $i_{D}$ (mA)',fontsize=14)
axes.set_xlabel('Voltaje $VGS$  (V)',fontsize=14)
axes.grid(True)
plt.savefig('JFET.jpg',dpi=500,bbox_inches='tight')