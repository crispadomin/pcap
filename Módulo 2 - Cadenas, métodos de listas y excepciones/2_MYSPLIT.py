
##########################
# Solución alternativa
##########################

def mysplit(strng):
    # devolver [] si la cadena está vacía o solo contiene espacios en blanco
    if strng == '' or strng.isspace():
        return [ ]
    # preparar una lista para devolver
    lst = []
    # preparar una palabra para construir palabras subsecuentes
    word = ''
    # verificar si actualmente estamos dentro de una palabra 
    # (es decir, si la cadena comienza con una palabra)
    inword = not strng[0].isspace()
    # iterar a través de todos los caracteres en cadena
    for x in strng:
          # si actualmente estamos dentro de una cadena ...
        if inword:
            # ... y el carácter actual no es un espacio ...
            if not x.isspace():
                # ... actualizar palabra actual
                word = word + x
else:
                # ... de lo contrario, llegamos al final de la palabra, 
                # por lo que debemos agregarla a la lista ...
                lst.append(word)
                # ... y señalar que estamos ahora fuera de la palabra
                inword = False
        else:
            # si estamos fuera de la palabra y llegamos a un carácter no que no es un espacio en blanco
            if not x.isspace():
                # ... significa que ha comenzado una nueva palabra, por lo que debemos recordarla y ...
                inword = True
                  # ... almacenar la primera letra de la nueva palabra
                word = x
            else:
                pass
        # si hemos dejado la cadena y hay una cadena no vacía en la variable word, necesitamos actualizar la lista
    if inword:
        lst.append(word)
    # devolver la lista a invocador
    return lst

Susana Navarro Caravaca  a  Todos 9:00
Buenos días

César Martín  a  Todos 9:00
print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

##########################
# Solución alternativa
##########################

# def mysplit(cadena):

#     lista_palabras = []

#     palabra = ''

#     for caracter in cadena:
    
#         if caracter != ' ':
#         # if not caracter.isspace():
#             palabra += caracter
#         else:
#             lista_palabras.append(palabra)
#             palabra = ''  
        
#     lista_palabras.append(palabra)
    
#     return lista_palabras

#################################3

# cadena = input("Introduce una cadena de caracteres: ")

# print(mysplit(cadena))

##########################
# Solución alternativa
##########################

# def mysplit(strng):
    
#     pos_find = strng.find(' ')
#     if pos_find == -1:
#         return [strng]
#     else:
#         return [strng[:pos_find]] + mysplit(strng [pos_find + 1:])