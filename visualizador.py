# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:02:54 2023

@author: the8t
"""

import numpy as np
import matplotlib.pyplot as plt
import random

plt.rcParams['text.usetex'] = True

S = 1000
a = 1
N = int(input("Ingrese la cantidad de pasos que desea que el caminante aleatorio ejecute: ")) #Se crean los conjuntos vacios de datos a lo largo de las tres direcciones espaciales usando el parámetro de numero de pasos N

Dir = ["x+","x-","y+","y-","z+","z-"] #Se define las seis posibles direcciones: dos a lo largo de cada uno de los ejes cartesianos.

X = np.zeros(N)
Y = np.zeros(N)
Z = np.zeros(N)

for i in range(1,N): #Se crea la iteración del caminante, usando para este fin el parámetro de pasos N.
    salto = random.choice(Dir) #Se usa la función randomizadora para seleccionar, con igual probabilidad, cualquiera de las direcciones espaciales definidas con anterioridad.
    if salto == "x+":  # Se crea un condicional para cada uno de los resultados del randomizador.
        X[i] = X[i-1] + a 
        Y[i] = Y[i-1]
        Z[i] = Z[i-1]
    elif salto == "x-":
        X[i] = X[i-1] - a
        Y[i] = Y[i-1]
        Z[i] = Z[i-1]   
    elif salto == "y+":
        X[i] = X[i-1]
        Y[i] = Y[i-1] + a
        Z[i] = Z[i-1]
    elif salto == "y-":
        X[i] = X[i-1]
        Y[i] = Y[i-1] - a
        Z[i] = Z[i-1]
    elif salto == "z+":
        X[i] = X[i-1]
        Y[i] = Y[i-1]
        Z[i] = Z[i-1] + a
    elif salto == "z-":
        X[i] = X[i-1]
        Y[i] = Y[i-1]
        Z[i] = Z[i-1] - a

plt.figure(figsize=[11,7])
ax = plt.subplot(1,1,1,projection='3d')
ax.plot(X,Y,Z,alpha=0.9)
ax.scatter(X[-1],Y[-1],Z[-1])
ax.set_xlabel(r'$X$',fontsize=17)
ax.set_ylabel(r'$Y$',fontsize=17)
ax.set_zlabel(r'$Z$',fontsize=17)
ax.text2D(0.05,0.95,"Visualización de Marcha Aleatoria",transform=ax.transAxes,fontsize=17)
plt.show()