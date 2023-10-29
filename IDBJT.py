# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 02:00:00 2020

@author: Rogelio Higuera
"""

import numpy as np
VD = 1.7
VT = 25e-3
Is = 1e-10
n=2
ID = Is*(np.exp(VD/(n*VT))-1)
print(ID)
