# ##############################---Excepción generada por Python---##########################

# def fun1(numero):
#     print("Ejecutando fun1() antes")
#     try:
#         fun2(numero)
#     except ZeroDivisionError:
#         print("Excepción ZeroDivisionError capturada en fun1()")       
#         raise
#     print("Ejecutando fun1() después")
    
# def fun2(numero):
#     print("Ejecutando fun2() antes")
#     try:        
#         fun3(numero)
#     except ZeroDivisionError:
#         print("Excepción ZeroDivisionError capturada en fun2()")       
#         raise                       #Para notificar de la excepción a la función invocadora



############################---Generando una excepciión propia---###############################
    
# class ValorInvalido(Exception):
#     pass

# ###########################################################

# def fun1(numero):
#     print("Ejecutando fun1() antes")
#     try:
#         fun2(numero)
#     except ValorInvalido:
#         print("Excepción ValorInvalido capturada en fun()")       
#         raise
#     print("Ejecutando fun1() después")
    
# def fun2(numero):
#     print("Ejecutando fun2() antes")
#     try:        
#         fun3(numero)
#     except ValorInvalido:
#         print("Excepción ValorInvalido capturada en fun2()")       
#         raise

#     print("Ejecutando fun2() después")

#     print("Ejecutando fun2() después")
    
# def fun3(numero):
#     print("Ejecutando fun3() antes")
    
#     try:
#         fun4(numero)
#     except ZeroDivisionError:
#         print("Excepción ZeroDivisionError capturada en fun3()")       
#         raise
#     print("Ejecutando fun3() después")

# def fun4(numero):
#     print("Ejecutando fun4() antes")
#     try:
#         resultado = numero / 0
#     except ZeroDivisionError:
#         print("Excepción ZeroDivisionError capturada en fun4()")       
#         raise

# ##############################################################

# try:
#     fun1(20000)
# except ZeroDivisionError:
#     print("Excepción ZeroDivisionError capturada en el programa principal")
        
# ########################################################



# def fun3(numero):
#     print("Ejecutando fun3() antes")
    
#     try:
#         fun4(numero)
#     except ValorInvalido:
#         print("Excepción ValorInvalido capturada en fun3()")       
#         raise
#     print("Ejecutando fun3() después")

# def fun4(numero):
#     print("Ejecutando fun4() antes")
#     try:
#         if numero >= 1000:
#             raise ValorInvalido
            
#     except ValorInvalido:
#         print("Excepción ValorInvalido capturada en fun4()")       
#         raise
# ##############################################################

# try:
#     fun1(20000)
# except ValorInvalido:
#     print("Excepción ValorInvalido capturada en el programa principal")


#######################################################################

class SalarioInvalido(Exception):
    pass

salario_ok = 0

while(salario_ok == 0):
    salario = input("Introduce la cantidad del salirio (1000€ - 5000€): ")
    try:
        if int(salario) < 1000 or int(salario) > 5000:
            raise SalarioInvalido
        else:
            print("El salario introducido es correcto.")
            salario_ok = 1
            break
    # except SalarioInvalido:
    #     print("El salario introducido no es correcto. Por favor, intorudce una cantidad correcta.")
    # except ValueError:
    #     print("El dato introducido no es correcto. Por favor, intorudce un número.")
    except Exception as ex:         #Para conocer información sobre la expección capturada
        print("\tExcepción:", type(ex).__name__)
        print('\t',ex)
        print("Ha ocurrido un error desconocido.")



##########################---ASSERTIONS---#############################
# import math

# x = float(input("Ingresa un número: "))
# assert x >= 0.0

# x = math.sqrt(x)

# print(x)

