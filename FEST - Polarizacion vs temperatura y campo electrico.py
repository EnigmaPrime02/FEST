# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:13:40 2023

@author: the8t
"""

import numpy as np 
import matplotlib.pyplot as plt

plt.style.use('ggplot') #Fondo gris para las graficas
plt.rcParams['text.usetex'] = True #Activar notación de LaTeX para las graficas

V = 1 # m^3 (Vólumen del contenedor)
Kb = 1.380649e-23 # m^2 kg s^-2 K^-1 (Constante de Boltzmann)
mu = 6.17e-30 # C m (Orden de magnitud de momento dipolar)
N = 6.0221408e+23 #Moléculas (# de Avogadro)

EM = [100,200,300,400,500,1000,2000]
TEMP = [1,10,100,300,500,1000,2000]

def Pol_E(E,T):
    return (N*Kb*T)/(E*V)*((mu*E)/(Kb*T)*1/np.tanh(mu*E/(Kb*T))-1)

Ti = np.linspace(100,500,1000)
Pi = []
for i in range(len(EM)):
    p_i = Pol_E(EM[i],Ti)
    Pi.append(p_i)

Ei = np.linspace(1,1e+3,1000)
Pi2 = []
for i in range(len(TEMP)):
    p_i2 = Pol_E(Ei,TEMP[i])
    Pi2.append(p_i2)


###########################################
Viridis = ['#fde725','#90d743','#35b779','#21918c','#31688e','#443983','#440154']

plt.figure(figsize=[11,7])

for i in range(len(Pi)):
    plt.plot(Ti,Pi[i],color=Viridis[i],label=f'$E={EM[i]}\,(N/C)$')


plt.title(r'$\textrm{Polarización promedio vs. Temperatura}$',fontsize=23)
plt.xlabel(r'$T\,(K)$',fontsize=19)
plt.ylabel(r'$\log_{10}(\vec{P}):=\log_{10}\left(\langle\vec{\mu}\rangle/V\right)\,\,(C\cdot m)$',fontsize=19)
plt.yscale("log")
plt.legend(prop={'size': 17})
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)