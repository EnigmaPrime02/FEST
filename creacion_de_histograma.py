# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 00:48:27 2023

@author: Juan José Mejía A.
"""

"""
Se empieza con la inicialización de las librerías:
    
    numpy para funciones numéricas básicas y álgebra lineal
    matplotlib.pyplot para el graficado de las funciones
    random para la aleatoreidad deseada
"""

import numpy as np
import matplotlib.pyplot as plt
import random


plt.rcParams['text.usetex'] = True

S = 1000
a = 1
N = int(input("Ingrese la cantidad de pasos que desea que el caminante aleatorio ejecute: ")) #Se crean los conjuntos vacios de datos a lo largo de las tres direcciones espaciales usando el parámetro de numero de pasos N

Dir = ["x+","x-","y+","y-","z+","z-"] #Se define las seis posibles direcciones: dos a lo largo de cada uno de los ejes cartesianos.
DIST = [] #Se crea una lista vacía en la que se introducirán las distancias finales para cada una de las iteraciones de caminante aleatorio.

for j in range(0,S):
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
    dist = np.sqrt(X[N-1]**2+Y[N-1]**2+Z[N-1]**2)#Se calcula la distancia euclidea usual
    DIST.append(dist)#Por cada una de las iteraciones, se guarda la distancia computada del último paso dado por el caminante

plt.figure(figsize=[9,6])#Se define el ambiente de figura usando pyplot. La escala escogida es 3:2
cm = plt.cm.get_cmap('RdYlBu_r') #Mapa de color para histograma

Y,X = np.histogram(DIST, 25, density=True) #Se crea el mapa de histograma
x_span = X.max()-X.min() #Se define el intervalo de cada una de las barras
C = [cm(((x-X.min())/x_span)) for x in X] #Se crea el mapa de colores para indicar con rojo los valores altos y con azul, los valores bajos.

plt.bar(X[:-1],Y,color=C,width=X[1]-X[0])
plt.title(r'$\textrm{Simulación de caminante aleatorio}$',fontsize = 17)
plt.xlabel(r'$\textrm{Distancia al origen (m)}$',fontsize=15)
plt.ylabel(r'$\textrm{Frecuencia normalizada}$',fontsize=15)
plt.show()