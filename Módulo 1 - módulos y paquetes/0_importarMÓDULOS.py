##############################################

import math                 # Necesario usar el prefijo del módulo
print(math.sin(math.pi/2))  # antes del nombre de la entidad

##############################################

from math import sin, pi    # Posibilidad de usar las entidades importadas
print(sin(pi/2))            # sin el prefijo del módulo ¡¡¡MEJOR!!!

##############################################

from math import *        # Se pueden usar todas las entidades del módulo
                            # sin el prefijo. ¡¡¡CUIDADO!!!

##############################################

import math as m            # Importar el módulo con un alias
print(m.sin(m.pi/2))

##############################################

from math import pi as PI, sin as sine  # También se puede asignar un alias a las entidades
print(sine(PI/2))

##############################################

import math
print(dir(math))            # Imprime la lista compelta de identificadores del módulo

for name in dir(math):      # Imprime la lista completa de manera vertical
    print(name)
