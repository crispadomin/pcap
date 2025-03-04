############################CIERRES############################
############################CIERRES############################
############################CIERRES############################

# def crear_funcion_potencias(parametro):
#     exponente = parametro

#     def potencia(base):
#         return base ** exponente
    
    
#     return potencia

# #######################################
# cuadrado = crear_funcion_potencias(2)
# cubo = crear_funcion_potencias(3)

# for i in range(5):
#     print(i, cuadrado(i), cubo(i))

############################--Ejemplo cierre--############################

def fabrica_funciones(potencia, limite):
    __potencia = potencia
    __limite = limite

    def fun_lista_potencias():
        return [numero ** __potencia for numero in range(__limite)]     # Es una lista porque está entre corchetes

    def fun_generador_potencias():
        return (numero ** __potencia for numero in range(__limite))     # Es un generador porque está entre paréntesis

    return fun_lista_potencias if __limite < 100 else fun_generador_potencias

########################################################
# listas de 10 elementos elevados al cuadrado y al cubo
########################################################

cuadrados = fabrica_funciones(potencia=2, limite=10)

lista_cuadrados = cuadrados()

print(lista_cuadrados)    

cubos = fabrica_funciones(potencia=3, limite=10)    

lista_cubos = cubos()

print(lista_cubos)    

##############################################################
# generadores de 100 elementos elevados al cuadrado y al cubo
##############################################################

cuadrados = fabrica_funciones(potencia=2, limite=100)

for valor in cuadrados():       # Para imprimir lso generadores hay que procesarlos a partir de bucle
    print(valor, end =' ')

cubos = fabrica_funciones(potencia=3, limite=100)    
for valor in cubos():
    print(valor, end =' ')