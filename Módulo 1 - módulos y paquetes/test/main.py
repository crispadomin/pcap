

from sys import path
# path.append('C:\\Users\\crisp\\Desktop\\PUE\\Python\\Prácticas\\Essentials 2\\modules')
path.append('..\\modules')

from module import suml, prodl, __counter

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

print("Número de llamadas a la función:", __counter)

# Todos los directorios donde busca los módulos
# import sys
# for p in sys.path:
#     print(p)

