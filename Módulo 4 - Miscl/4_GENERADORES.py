##########################--Ejemplo generador--###############################

# class Generador:
#     def __init__(self, limite):
#         print("__init__")
#         self.__limite = limite
#         self.__valor_actual = 0

#     def __iter__(self):         # debe devolver el objeto en sí y que se invoca una vez (es necesario que Python inicie correctamente la iteración)
#         print("__iter__")
#         return self

#     def __next__(self):         # debe devolver el siguiente valor (primero, segundo, etc.) de la serie deseada
#         print("__next__")		
#         self.__valor_actual += 1
#         if self.__valor_actual > self.__limite:     # para pasar a la siguiente iteración (siguiente valor)
#             raise StopIteration                     # si no hay más valores para proporcionar, el método generará la excepción
#         return self.__valor_actual


# for numero in Generador(10):
#     print(numero)


##########################--Ejemplo generador--###############################

# class Generador:
#     def __init__(self, limite):
#         print("__init__")
#         self.__limite = limite
#         self.__valor_actual = 0

#     def __iter__(self):
#         print("__iter__ en Generador")
#         return self                     # Devuelve el objeto generador

#     def __next__(self):
#         print("__next__")		
#         self.__valor_actual += 1
#         if self.__valor_actual > self.__limite:
#             raise StopIteration
            
#         return self.__valor_actual

# class Clase1:
#     def __init__(self, limite):
#         self.__x = Generador(limite)

#     def __iter__(self):
#         print("__iter__ en Clase1")
#         return self.__x                 # Devuelve el objeto generador, en este caso, se ejecutará el __next__ de la clase Generador
# ###################################
# objeto = Clase1(8)
# for i in objeto:
#     print(i)

##########################--Crear generador con yield--###############################

# def fun(n):
#     for i in range(n):
#         yield i


# for v in fun(5):
#     print(v)

##########################--Crear generador con yield--###############################

# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# for v in powers_of_2(8):
#     print(v)

##########################--Crear generador con yield--###############################
##########################--Con LIST COMPREHENSION--###############################
# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# t = [x for x in powers_of_2(5)]
# print(t)

##########################--Crear generador con yield--###############################
##########################--Con función LIST()--###############################
# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# t = list(powers_of_2(3))
# print(t)

##########################--Crear generador con yield--###############################
##########################--Con operador in--###############################
# def powers_of_2(n):
#     power = 1
#     for i in range(n):
#         yield power
#         power *= 2


# for i in range(20):
#     if i in powers_of_2(4):
#         print(i)


##########################--lIST COMPREHENSION--###############################
# the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
# the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

# for v in the_list:
#     print(v, end=" ")
# print()

# for v in the_generator:
#     print(v, end=" ")
# print()

##########################--EJEMPLO PILA 1--###############################
lista = [x for x in range(20)]

def get_list(list):
    for i in range(len(list)):
        yield i

for i in get_list(lista):
    if i%2 == 0:
        lista.remove(i)
        print("Eliminamos ", i, ". La lista queda ", lista, sep ='')

##########################--EJEMPLO PILA 2--###############################
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def quitar_pares_yield(lista):    
#     for n in lista:
#         if n  % 2 != 0:
#             yield n

# for x in quitar_pares_yield(lista):
#     print(x)

# ##########################--EJEMPLO PILA 3--###############################
# pila = [1,2,3,4,5]

# def extraer_elemento(lista_pila:list):
#     for n in range(len(lista_pila)):
#         yield lista_pila[len(pila) -n -1]

# for elemento in extraer_elemento(pila):
#     print(elemento)

# ##########################--EJEMPLO PILA 4--###############################
# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)
#         print(f"Elemento '{item}' agregado a la pila: {self.items}")

#     def __iter__(self):
#         # Imprimir la lista completa antes de empezar a retirar elementos
#         print("Lista completa antes de retirar elementos:", self.items)
#         # Utilizar yield para devolver los elementos uno por uno
#         while self.items:
#             yield self.items.pop()
#             print(f"Elemento '{item}' retirado de la pila: {self.items}")

# # Ejemplo de uso:
# stack = Stack()

# for i in range(1,10):
#     stack.push(i)

# # Utilizar un bucle for para retirar los elementos de la pila e imprimirlos
# print("\nElementos retirados de la pila:")
# for item in stack:
#     print(item)