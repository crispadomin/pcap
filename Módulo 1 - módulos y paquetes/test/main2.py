# Paso 7

# from sys import path
# path.append('..\\packages') # Windows
# # path.append('../packages') # MacOS - Unix - Linux

# import extra.iota

# print(extra.iota.funI())

# # Alternativa

# from sys import path
# # path.append('..\\packages') # Windows
# path.append('../packages') # MacOS - Unix - Linux

# from extra.iota import funI
# print(funI())

# Paso 8

# from sys import path

# # path.append('..\\packages') # Windows
# path.append('../packages') # MacOS - Unix - Linux

# import extra.good.best.sigma
# from extra.good.best.tau import funT

# print(extra.good.best.sigma.funS())
# print(funT())


# con alias (éste ejemplo falla en Spyder, probar con IDLE)

# from sys import path

# path.append('..\\packages') # Windows
# path.append('../packages') # MacOS - Unix - Linux

# import extra.good.best.sigma as sig
# import extra.good.alpha as alp

# print(sig.funS())
# print(alp.funA())

# import os 
# print(os.path.abspath(os.getcwd()))

# Paso 9 (éste ejemplo falla en Spyder, probar con IDLE)

from sys import path

path.append('..\\packages\\extrapack.zip')   # Windows
# path.append('../packages/extrapack.zip')       # MacOS - Unix - Linux

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())

