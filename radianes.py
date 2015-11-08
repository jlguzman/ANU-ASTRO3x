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