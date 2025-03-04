##############################################

# platform(aliased = False, terse = False)

# aliased → cuando se establece a True (o cualquier valor distinto a cero) 
# puede hacer que la función presente los nombres de capa subyacentes 
# alternativos en lugar de los comunes.

# terse → cuando se establece a True (o cualquier valor distinto a cero) 
# puede convencer a la función de presentar una forma más breve del resultado 
# (si fuera posible).

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

##############################################

# identificación del nombre genérico del procesador

from platform import machine

print(machine())

##############################################

# identificación del nombre específico del procesador (CPU)

from platform import processor

print(processor())

##############################################

# identificación de la versión del sistema operativo

from platform import version, uname

print(version())
print(uname())

##############################################

# identificación de la versión del sistema operativo

from platform import version, uname

print(version())
print(uname())
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr, '.',end='', sep='')