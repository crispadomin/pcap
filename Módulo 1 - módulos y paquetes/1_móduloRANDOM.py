##############################################

from random import random   # random() produce un número flotante x entre el rango (0.0, 1.0)

for i in range(5):
    print (random())

##############################################

from random import random, seed

seed(0)                     # seed() establece la semilla del generador
                            # seed(int_value) establece la semilla con el valor entero int_value
for i in range(5):
    print(random())

# Si la semilla siempre se establece con el mismo valor,
# la secuencia de valores generados siempre se ve igual.
    
##############################################

from random import randrange, randint
# Si se quieren valores aleatorios enteros
print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')          # randrange(inicio, fin, incremento)
print(randint(0, 1))

print(randrange(10), end=' ')               # randrange(inicio) de 0 a 9
print(randrange(0, 10), end=' ')            # randrange(inicio, fin) de 0 a 9
print(randrange(0, 10, 3), end=' ')         # randrange(inicio, fin, incremento) de 0 a 9, de 3 en 3

print(randint(0, 1))    # sin excluir el valor máximo

##############################################

from random import choice, sample

#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]

print(choice(my_list))
print(sample(my_list, 5))                   # Sin repetición de los valores
print(sample(my_list, 10))                  # Sin repetición de los valores