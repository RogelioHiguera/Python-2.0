# -*- coding: utf-8 -*-
"""
Editor de Spyder
Tecnológico Nacional de México (TECNM)
Tecnológico de Estudios Superiores de Ixtapaluca (TESI)
División de ingeniería electrónica
Introducción a la librería Numpy 1
M. en C. Rogelio Manuel Higuera Gonzalez
"""
##################################################################################
import numpy as np #Cargar la librería Numpy
##################################################################################
lista1 = [1,2,3,4,5] #Crear una lista en Python
a1 = np.arange(10) #Crea un arreglo espaciado uniformemente con un intervalo dado
a2 = np.arange(0,10,2) #Crea un arreglo de 0 a 8 con espaciado de 2
a3 = np.zeros(5) #Crea un arreglo de ceros con cinco elementos
a4 = np.zeros((2,3)) #Crea un arreglo 2X3 de ceros
a5 = np.full((2,3),8) #Crea un arreglo 2X3 de ochos
a6 = np.eye(4) #Crea un arreglo de una matriz identidad
##################################################################################
lista2 = [5,4,3,2,1]
b1 = np.array(lista2) #Crea un arreglo de una lista
b2 = np.array ([lista1,lista2]) #Crea un arreglo 2X5 de dos listas
b3 = b2[0,0] #Elemento de la primera fila y la primera culumna
b4 = b1[[2,4]] #Elementos de la  fila 3 y 5
##################################################################################
b5 = b1>2 #Crea un arreglo booleano, True si el elemento del arreglo b1 es mayor a 2 y False de caso contrario
b6 = b1[b1>2] #Crea un arreglo con los elementos mayores a 2 de b1
nums = np.arange(20) #Crea un arreglo de 20 elementos de 0 a 19
add_nums = nums[nums % 2 == 1] #Crea un arreglo de los elementos impares del arreglo nums
##################################################################################
c1 = np.array([[1,2,3,4,5],[4,5,6,7,8],[9,8,7,6,5]]) #Crea un arreglo 3X5
c2 = c1[1:3,:3] #El indice final no esta incluido en la respuesta [start:stop,start:stop]
c3 = c1[-2:,-2:] #indice negativo
c4 = np.array([9,8,7,6,5])
c5 = c4.reshape(1,-1) #El primer 1 indica que quieres convertirlo a un arreglo de rango 2 y el -1 indica que lo dejaras en manos de la función reshape() para crear el numero de columnas
c6 = c4.reshape(-1,) #El -1 indica que dejaste que la función decida cuantas filas crear, siempre y cuando el resultado final tenga un arreglo con rango 1

 

