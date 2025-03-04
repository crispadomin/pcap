########################################################
########################################################

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy


# sun = Star("Sol", "Vía Láctea")
# print(sun)

########################################################

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + ' en ' + self.galaxy


# sun = Star("Sol", "Vía Láctea")
# print(sun)

##########################--ISSUBCLASS--##############################

# class Vehicle:
#     pass


# class LandVehicle(Vehicle):
#     pass


# class TrackedVehicle(LandVehicle):
#     pass


# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")
#     print()
    
##########################--ISINSTANCE--##############################
    
# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()

# for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj, cls), end="\t")
#     print()

##########################--IS--##############################

# class SampleClass:
#     def __init__(self, val):
#         self.val = val


# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1         # Se crea object3 apuntando a la misma dirección que object1
# object_3.val += 1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val, object_2.val, object_3.val)

# string_1 = "Mary tenía un "
# string_2 = "Mary tenía un corderito"
# string_1 += "corderito"

# print(string_1 == string_2) # Son el mismo valor?
# print(string_1 is string_2) # Apuntan a la misma dirección?

# # string_1 y string_2 son dos objetos distintos, tienen diferente id
# print(id(string_1))
# print(id(string_2))

##########################--__eq__--##############################

# class SampleClass:
#     def __init__(self, val):
#         self.val = val


# object_1 = SampleClass(0)
# object_2 = SampleClass(1)
# object_3 = object_1
# object_3.val += 1

# print('object_1 is object_2:', object_1 is object_2)
# print('object_1 == object_2:', object_1 == object_2)

# print('object_2 is object_3:', object_2 is object_3)
# print('object_2 == object_3:', object_2 == object_3)

# print('object_3 is object_1:', object_3 is object_1)
# print('object_3 == object_1:', object_3 == object_1)

# print(object_1.val, object_2.val, object_3.val)

# string_1 = "Mary tenía un "
# string_2 = "Mary tenía un corderito"
# string_1 += "corderito"

# print(string_1 == string_2, string_1 is string_2)

##########################--__str__--##############################

# Como no existe el método __str__() dentro de la clase Sub,
# la cadena a imprimir se producirá dentro de la clase Super.
# Esto significa que el método __str__() ha sido heredado por la clase Sub.

# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "SUPER - Mi nombre es " + self.name + "."


# class Sub(Super):
#     # def __init__(self, name):
#     #     Super.__init__(self, name)
    
#     def __str__(self):
#         return "SUB - Mi nombre es " + self.name + "."


# obj = Sub("Andy")

# print(obj)

# ##########################--HERENCIA SIMPLE--##############################

# class Level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101

#     def fun_1(self):
#         return 102


# class Level2(Level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
    
#     def fun_2(self):
#         return 202


# class Level3(Level2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301

#     def fun_3(self):
#         return 302


# obj = Level3()

# print(obj.variable_1, obj.var_1, obj.fun_1())
# print(obj.variable_2, obj.var_2, obj.fun_2())
# print(obj.variable_3, obj.var_3, obj.fun_3())

##########################--HERENCIA MÚLTIPLE--##############################

# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11

# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21

# class Sub(SuperA, SuperB):
#     pass


# obj = Sub()

# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())

##########################--HERENCIA MÚLTIPLE--##############################
##############################--ejemplo--##################################

class Super1:
#     def __init__(self, name):
#         self.name = name + 'Super1'
#         print('Constructor de Super1')

#     def __str__(self):
#         return "Mi nombre es " + self.name + "."

# class Super2:
#     def __init__(self, name):
#         self.name = name + 'Super2'
#         print('Constructor de Super2')

#     def __str__(self):
#         return "Mi nombre es " + self.name + "."

# class Sub(Super1, Super2):
#     def __init__(self, name):
#         super().__init__(name)
        
#         # Super1.__init__(self, name)
#         # Super2.__init__(self, name)

##############################--ejemplo--##################################
    
# obj = Sub("Andy")

# print(obj)
# print(obj.__dict__)


# import time

# class Cadenas:
#     def cambiar_direccion(self, izquierda, encendido):
#         print("pistas: ", izquierda, encendido)


# class Ruedas:
#     def cambiar_direccion(self, izquierda, encendido):
#         print("ruedas: ", izquierda, encendido)


# class Vehiculo:
#     def __init__(self, controlador):
#         self.controlador = controlador

#     def girar(self, izquierda):
#         self.controlador.cambiar_direccion(izquierda, True)
#         time.sleep(0.25)
#         self.controlador.cambiar_direccion(izquierda, False)


# ruedas = Vehiculo(Ruedas())
# cadenas = Vehiculo(Cadenas())

# cadenas.girar(True)
# ruedas.girar(False)

##############################--ejemplo--##################################

class Empleado:
    def __init__(self):
        self.__nombre = ''
        self.__apellido = ''
        self.__salario = 0
        self.Cargo = Cargo.get(self.__nombre)
    
    def cambiar_cargo (self, self.Cargo, cargo_nuevo):


class Cargo:
    def __init__(self, nombre):
        self.__tipo_cargo = ''

    def calcular(self):
        pass

    def get():
        return self.__tipo_cargo
    
def Comercial(Cargo):
    def __init__(self):
        self.__salario = 0
        self.__ventas = 0

    def calcular(self):
        self.__salario += 1.15 * self.__ventas

