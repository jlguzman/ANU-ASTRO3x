# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:23:33 2015

@author: joseluisguzmanlidon
"""

"Una circunferencia son 2*pi radianes, luego para pasar de segundos a radianes"
"hay que pasar los grados "

import math

def radianes(segundos):
    return (segundos/60.0) *(1/60.0) * 2*math.pi/360.0
    
def m2_1(m1,r1,r2):
    return (m1*r1/r2)
    
def m2_2(r1, r2, P):
    G = 6.67384e-11
    return ((4*(math.pi)**2)/(G*(P**2))) * r1 * (r1 + r2)**2
    
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
    
#modificacion para probar el github