# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:05:30 2015

@author: joseluisguzmanlidon
"""

# HQ1.1

# 1 parsec son 3.09e16 metros
# r = D * phi, en donde r es el radio de giro, D la distancia y phi en rad

import jlfun

D = 3.09e16 * 5
phi = jlfun.radianes(10.0)

radio = D * phi

#HQ1.2
# Calcular la masa del objeto estelar no visible dados el Radio, la masa y 
# el período de rotación del objeto visible que gira en torno de él

# Las ecuaciones son m1*R1 = m2*R2 y m2=((4*pi^2)/G*P^2)*r1*(r1+r2)^2 
# para utilizar el paquete simbóloco llamo "x" a m2 e "y" a r2
# las ecuaciones quedan así:
#   x*y - m1*r1 = 0
#   (((4*pi^2)/G*P^2)*r1*(r1+r2)^2) - x = 0 

#from sympy import solve_poly_system
#from sympy import *

#x, y, z, t = symbols('x y z t')

m1 = 3.0e30    # masa de la estrella visible
P = 100 * 365 * 24 * 3600   # período de rotación de la estrella visible, en segundos
R1 = 1.02e12        # radio de la estrella visible
G = 6.67384e-11     #Constante de Gravitación universal en N*m^2/kg^2
AU = 1.496e11       #Unidad Astronómica

#solve([Eq(x*y - 3.0e30*1.0e12,0), Eq((((4*3.141592**2)/6.67384e-11*(3153600000**2))*1.0e12*(1.0e12+y)**2) - x,0)], [x, y])

#Método de resolución por fuerza bruta
#Se van probando valores de masa para las dos ecuaciones supuesto un valor de r2
#se para cuando la diferencia entre ambos valores es inferior a un umbral

for d in jlfun.my_range(10, 25, 0.01):
    M21 = jlfun.m2_1(m1,R1,d*AU)
    M22 = jlfun.m2_2(R1, d*AU, P)
    print(M21, M22, d, M21/M22)
    
    if (M21/M22 > 0.99) &  (M21/M22 < 1.01):
        M2 = M21
        print(M2)
        break


#HQ1.3
#Calcular el tamaño de una "compañera invisible" dadas su temperatura (en Km)
# y luminosidad relativa respecto a la estrella visible que gira y la temperatura de la estrella
#visible

# En los problemas resueltos : (r1/r2)^2 = (L1/L2) * (T2/T1)^4
# Despejando: r2 = r1 / sqrt((L1/L2) * (T2/T1)^4)

T1 = 6000.0
r1 = 700000.0e3
T2 = 10000.0
L1L2 = 500.0 #L1/L2

r2 = r1 / math.sqrt((L1L2) * (T2/T1)**4)
r2 = r2 /1000.0


