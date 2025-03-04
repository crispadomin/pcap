##############################################--FUNCIÓN lambda--##############################################
# dos = lambda: 2
# cuadrado = lambda x: x * x
# potencia = lambda x, y: x ** y

# for a in range(10):
#     print('Cuadrado de', a, '=', cuadrado(a))
#     print('Potencia de', a,'elevado a 2:', potencia(a, dos()))

##############################################--FUNCIÓN lambda VS. def--##############################################

# def print_function(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')


# def poly(x):
#     return 2 * x**2 - 4 * x + 2


# print_function([x for x in range(-2, 3)], poly)

# ###########################################################################

# def print_function(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')

# print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

##############################################--FUNCIÓN lambda y map--##############################################
# list_1 = [x for x in range(5)]
# list_2 = list(map(lambda x: 2 ** x, list_1))
# print(list_2)

# for x in map(lambda x: x * x, list_2):
#     print(x, end=' ')
# print()

##############################################--FUNCIÓN lambda y filter--##############################################
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

