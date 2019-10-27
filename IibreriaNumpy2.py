# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 20:21:07 2019
Tecnológico Nacional de México (TECNM)
Tecnológico de Estudios Superiores de Ixtapaluca (TESI)
División de ingeniería electrónica
Introducción a la librería Numpy 2
M. en C. Rogelio Manuel Higuera Gonzalez
"""
import numpy as np
##################################################################################
ages = np.array([34,14,37,5,13]) #Crea un arreglo de edades
sorted_ages = np.sort(ages) #Acomoda los elementos del arreglo ages del menor al mayor
#ages.sort() #Acomoda los elementos del arreglo original ages del menor al mayor
argages = ages.argsort() #Indica el indice que clasifica a cada uno de los elementos del arreglo ages (del menor al mayor)
ages1 = ages[ages.argsort()] #Crea un arreglo ages ordenado dependiendo de su indice
##################################################################################


