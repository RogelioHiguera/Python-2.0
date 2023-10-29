# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 00:18:46 2022

@author: Rogelio Higuera
"""
import numpy as np
import matplotlib.pyplot as plt
Vd1 = np.array([-2, 0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2])
id1 = np.array([0, 0, 0.0001e-3, 0.0123e-3, 0.6031e-3, 9.365e-3, 14.164e-3,
                25.84e-3, 42.54e-3, 54.02e-3, 65.05e-3, 92.53e-3])
fig, axes = plt.subplots()
axes.plot(Vd1,id1*1e3,linewidth=2)
axes.set_ylabel('Corriente $i_{D}$ (mA)',fontsize=14)
axes.set_xlabel('Voltaje $VD$  (V)',fontsize=14)
axes.grid(True)
plt.savefig('Diodo.jpg',dpi=500,bbox_inches='tight')
