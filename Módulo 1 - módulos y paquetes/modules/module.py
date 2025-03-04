# print("Me gusta ser un módulo.")
# print(__name__)

# counter = 0

# if __name__ == "__main__":                  # si se ejecuta directamente el fichero de definicion de modulo
#     print("Me estoy ejecutando de manera independiente")

# else:
#     print("Me estoy ejecutando como un modulo")


###################### Paso 9 ##############################
#!/usr/bin/env python3 

""" module.py - Un ejemplo de un módulo en Python """

__counter = 0


def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter    
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero puedo realizar algunas pruebas por ti")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
    print("Número de llamadas a la función:", __counter)
