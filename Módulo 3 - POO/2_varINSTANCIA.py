##########################################################################################
##############################---3.3.1.1 POO: Propiedades---##############################
##########################################################################################

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val

#     def set_second(self, val):
#         self.second = val

# ##################################################

# example_object_1 = ExampleClass()   # fisrt = 1     objeto1
# example_object_2 = ExampleClass(2)  # first = 2     objeto2

# example_object_2.set_second(3)      # second = 3    objeto2

# example_object_3 = ExampleClass(4)  # first = 4      objeto3
# example_object_3.third = 5          # third = 5      objeto3    Se puede crear un atributo nuevo fuera de la clase, éste no puede ser privado.
#                                     #                           Este atributo se llama VARIABLE DE INSTANCIA                            
# #Información que contiene un objeto
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

##########################################################################################
#################################---ATRIBUTOS PRIVADOS---#################################
##########################################################################################

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.__first = val

#     def set_second(self, val = 2):
#         self.__second = val


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)

# example_object_2.set_second(3)

# example_object_3 = ExampleClass(4)
# example_object_3.__third = 5

# ##################################################
# print(example_object_1.__dict__)        # {'_ExampleClass__first': 1} -- NAME MANGLIG: debe accederse al atributo privado colocando una '_' delante del nombre de la clase
# print(example_object_2.__dict__)        # {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
# print(example_object_3.__dict__)        # {'_ExampleClass__first': 4, '__third': 5} -- La variable de isntancia no es privada, aunque incorpore '__'

##########################################################################################
#################################---VARIABLE DE CLASE---#################################
##########################################################################################

# class ExampleClass:
#     counter = 0                         # VARIABLE DE CLASE: común a todos los objetos de esa clase (porque NO es self.count)
#     def __init__(self, val = 1):        #                    es accesible antes de haber creado algún objeto de esa clase
#         self.__first = val
#         ExampleClass.counter += 1       # Para acceder a una variable de clase es necesario el accedo mediante el <nombre_clase>.var_clase


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)

# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)

# ExampleClass.counter = 400              # Para acceder a la variable de clase debe ser desde el nombre de la clase, no desde el nombre del objeto

# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)

##########################################################################################
#################################---VARIABLE DE CLASE---#################################
######################################-- PRIVADA --#######################################

# class ExampleClass:
#     __counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.__counter += 1


# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)

# print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
# print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
# print(example_object_3.__dict__, example_object_3._ExampleClass__counter)

##########################################################################################
#################################---ATRIBUTOS DE CLASE---#################################
######################################-propiedades-#######################################

# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1


# example_object = ExampleClass(1)
# print(example_object.a)

# try:
#     print(example_object.b)
# except AttributeError:
#     print("El atributo no existe.")

##########################################################################################
#################################---ATRIBUTOS DE CLASE---#################################
######################################-propiedades-#######################################
    
# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 19898


# example_object = ExampleClass(2)


# if hasattr(example_object, 'a'):
#     print('Valor de a', example_object.a)
    
# if hasattr(example_object, 'b'):
#     print('Valor de b', example_object.b)

########################################################
# class ExampleClass:
#     attr = 1

# print(hasattr(ExampleClass, 'attr'))
# print(hasattr(ExampleClass, 'prop'))

########################################################
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b')) # True
print(hasattr(example_object, 'a')) # True
print(hasattr(ExampleClass, 'b'))   # False
print(hasattr(ExampleClass, 'a'))   # True