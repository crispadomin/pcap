# # 1. Algunos de los métodos que ofrecen las cadenas son:

# # capitalize(): Convierte la inicial a Mayúsculas y el resto de la cadena a minúsculas.
# # center():     centra la cadena dentro de una longitud conocida.
# # count():      cuenta las ocurrencias de un carácter dado.
# # join():       une todos los elementos de una tupla/lista en una cadena.
# # lower():      convierte todas las letras de la cadena en minúsculas.
# # lstrip():     elimina los caracteres en blanco al principio de la cadena.
# # replace():    reemplaza una subcadena dada con otra.
# # rfind():      encuentra una subcadena comenzando por el final de la cadena.
# # rstrip():     elimina los caracteres en blanco al final de la cadena.
# # split():      divide la cadena en una subcadena usando un delimitador dado.
# # strip():      elimina los espacios en blanco iniciales y finales.
# # swapcase():   intercambia las mayúsculas y minúsculas de las letras.
# # title():      hace que la primera letra de cada palabra sea mayúscula.
# # upper():      convierte todas las letras de la cadena en letras mayúsculas.
# # endswith():   ¿La cadena termina con una subcadena determinada?
# # isalnum():    ¿La cadena consta solo de letras y dígitos?
# # isalpha():    ¿La cadena consta solo de letras?
# # islower():    ¿La cadena consta solo de letras minúsculas?
# # isspace():    ¿La cadena consta solo de espacios en blanco?
# # isupper():    ¿La cadena consta solo de letras mayúsculas?
# # startswith(): ¿La cadena comienza por un patrón determinado?


##########################################################

# str = """
#         cadena
#         entre
#         comillas
#         triples
#                 """

##########################################################

# str1 = 'a'
# str2 = 'b'

# print("str1 + str2:\t",str1 + str2)
# print("str2 + str1:\t", str2 + str1)

# print("5 * 'a':\t\t", 5 * 'a')
# print("'b' * 4:\t\t",'b' * 4)

# str1 += str2

# str2 *= 10

# print('str1 += str2:\t',str1)
# print('str2 *= 10:  \t', str2)

##########################################################

# # Demostración de la función ord ().

# char_1 = 'a'
# char_2 = ' '  # space

# print(ord(char_1))
# print(ord(char_2))

##########################################################

# # Demostración de la función chr.

# print(chr(97))
# print(chr(945))

##########################################################

# x = 'a'

# print(chr(ord(x)) == x)

# x = 90

# print(ord(chr(x)) == x)

##########################################################

# Indexando cadenas.

# the_string = 'silly walks'

# for ix in range(len(the_string)):
#     print(the_string[ix], end=' ')

# print()

# Cifrando cadenas.

# the_string = 'silly walks'
# coded_string = ''

# for ix in range(len(the_string)):
#     coded_string += ' ' + str(ord(the_string[ix]))
#     print(ord(the_string[ix]), end=' ')


# print(coded_string)

##########################################################

# Descifrando cadenas

# for numero in (coded_string.split(" ")):
#     if numero!= '':
#         print(chr(int(numero)),end='')
        
# descifrar
# print(mensaje_cifrado_con_espacios.split(' '))

# mensaje_descifrado = ''
# lista = mensaje_cifrado_con_espacios.split(' ')

# for indice in range(len(lista) - 1):
#     # print('bucle', lista[indice])
#     mensaje_descifrado += chr(int(lista[indice]))

# print(mensaje_descifrado)

##########################################################

# Iterando a través de una cadena.

# the_string = 'silly walks'

# for character in the_string:
#     print(character, end=' ')

# print()

##########################################################

# Rebanadas

# alpha = "abdefg"

# print("alpha[1:3]: ", alpha[1:3])
# print("alpha[3:]:  ", alpha[3:])
# print("alpha[:3]:  ", alpha[:3])
# print("alpha[3:-2]:", alpha[3:-2])
# print("alpha[-3:4]:", alpha[-3:4])
# print("alpha[::2]: ", alpha[::2])  # incremento!!!
# print("alpha[1::2]:", alpha[1::2]) # incremento!!!

##########################################################

# Operadores in / in not

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# print("f" in alphabet)
# print("F" in alphabet)
# print("1" in alphabet)
# print("ghi" in alphabet)
# print("Xyz" in alphabet)

# print("f" not in alphabet)
# print("F" not in alphabet)
# print("1" not in alphabet)
# print("ghi" not in alphabet)
# print("Xyz" not in alphabet)

##########################################################

# # Demonstrando min() - Ejemplo 1:
# print(min("aAbByYzZ"))


# # Demonstrando min() - Ejemplo 2 y 3:
# t = 'Los Caballeros Que Dicen "¡Ni!"'
# print('[' + min(t) + ']')

# t = [0, 1, 2]
# print(min(t))

##########################################################

# # Demostración de max() - Ejemplo 1:
# print(max("aAbByYzZ"))


# # Demostración de max() - Ejemplo 2 & 3:
# t = 'Los Caballeros Que Dicen "¡Ni!"'
# print('[' + max(t) + ']')

# t = [0, 1, 2]
# print(max(t))

##########################################################

# # Demonstrando el método index() --- primera vez que coincide:
# print("aAbByYzZaA".index("b"))
# print("aAbByYzZaA".index("Z"))
# print("aAbByYzZaA".index("A"))

##########################################################

# # Demostración de la función list():
# print(list("abcabc"))

# # Demostración de la count list():
# print("abcabc".count("b"))
# print('abcabc'.count("d"))

##########################################################

# # Demostración del método capitalize():
# print("Alpha".capitalize())
# print('ALPHA'.capitalize())
# print(' Alpha'.capitalize())
# print('123'.capitalize())
# print("αβγδ".capitalize())

# Demostración del método lower():
# print("SiGmA=60".lower())

##########################################################

# # Demostración del método center():

# print('[' + 'alpha'.center(10) + ']')

# print('[' + 'alpha'.center(10) + ']')

# for contador in range(10,15):
#     print('[' + 'alpha'.center(contador) + ']')

# # La variante de dos parámetros de center() hace uso del carácter del segundo argumento, en lugar de un espacio. Analiza el siguiente ejemplo:

# print('[' + 'gamma'.center(20, '*') + ']')

##########################################################

# # Demostración del método endswith():
# if "epsilon".endswith("on"):
#     print("si")
# else:
#     print("no")

# t = "zeta"
# print(t.endswith("a"))
# print(t.endswith("A"))
# print(t.endswith("et"))
# print(t.endswith("eta"))

# # Demostración del método startswith():
# t = "zeta"
# print(t.startswith("z"))

##########################################################

# # Demostración del método find():
# # Nota: no se debe de emplear find() si deseas verificar si un solo carácter aparece dentro de una cadena - el operador in será significativamente más rápido.

# print("Eta".find("ta"))
# print("Eta".find("mma"))

# t = 'theta'
# print(t.find('eta'))
# print(t.find('et'))
# print(t.find('the'))
# print(t.find('ha'))

# print('kappa'.find('a', 2))

# the_text = """A variation of the ordinary lorem ipsum
# text has been used in typesetting since the 1960s 
# or earlier, when it was popularized by advertisements 
# for Letraset transfer sheets. It was introduced to 
# the Information Age in the mid-1980s by the Aldus Corporation, 
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""

# posicion = the_text.find('the')
# while posicion != -1:
#     print(posicion)
#     posicion = the_text.find('the', posicion + 1)

##########################################################

# # Demostración del método the isalnum() - is alphanumeric or nubmer:

# print('lambda30'.isalnum())
# print('lambda'.isalnum())
# print('30'.isalnum())
# print('@'.isalnum())
# print('lambda_30'.isalnum())
# print(''.isalnum())

# t = 'Six lambdas'
# print(t.isalnum())

# t = 'ΑβΓδ'
# print(t.isalnum())

# t = '20E1'
# print(t.isalnum())

# # Ejemplo 1: Demostración del método isapha():

# print("Moooo".isalpha())
# print('Mu40'.isalpha())

# # Ejemplo 2: Demostración del método isdigit():

# print('2018'.isdigit())         #True
# print("Year2019".isdigit())     #False

##########################################################

# # Ejemplo 1: Demostración del método islower():
# print("Moooo".islower())
# print('moooo'.islower())

# # Ejemplo 2: Demostración del método isspace(:
# print(' \n '.isspace())
# print(" ".isspace())
# print("mooo mooo mooo".isspace())

# # Ejemplo 3: Demostración del método isupper():
# print("Moooo".isupper())
# print('moooo'.isupper())
# print('MOOOO'.isupper())

##########################################################

# # Demonstración del método join():
# print(",".join(["omicron", "pi", "rho"]))

# list = ['Yo', 'soy', 'Cristina', 'Parra']
# string = ' '.join(list)
# print(string, end='.\n')
# print(string.split(' '))

##########################################################

# # Demostración del método the strip() - elimina los espacios al inicio y final de la cadena:
# print("[" + " tau ".strip() + "]")

# # Demostración del método the lstrip() - elimina los espacios al inicio de la cadena:
# print("[" + " tau ".lstrip() + "]")

# # Demostración del método the rstrip() - elimina los espacios al final de la cadena:
# print("[" + " tau ".rstrip() + "]")
# print("cisco.com".rstrip(".com"))       #-elimina todos los caracteres finales que coinciden con lo especificado entre paréntesis

##########################################################

# # Demostración del método replace():
# print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
# print("This is it!".replace("is", "are"))
# print("Apple juice".replace("juice", ""))

# print("This is it!".replace("is", "are", 1))    # Sólo reemplaza el 1º encontrado
# print("This is it!".replace("is", "are", 2))

##########################################################

# # Demostración del método rfind() - empezando a buscar por el final:
# print("tau tau tau".rfind("ta"))
# print("tau tau tau".rfind("ta", 9))
# print("tau tau tau".rfind("ta", 3, 9))

##########################################################

# # Demostración del método swapcase():
# print("Yo sé que no sé nada.".swapcase())

# # Demostración del método title():
# print("Yo sé que no sé nada. Part 1.".title())

# # Demostración del método upper():
# print("Yo sé que no sé nada. Part 2.".upper())

##########################################################

 # Demostración de comparación de cadenas de caracteres

# print('10' == '010')
# print('10' > '010')
# print('10' > '8')
# print('20' < '8')
# print('20' < '80')
# print('10' == 10)
# print('10' != 10)
# print('10' == 1)
# print('10' != 1)
# print('10' > 10) # TypeError!!!

##########################################################

# # Demostración de la función sorted() - crea una lista nueva:
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)

# print(first_greek)
# print(first_greek_2)

# print()

# # Demostración del método sort() - ordena la lista actual (no válido para tuplas):
# second_greek = ['omega', 'alpha', 'pi', 'gamma']
# print(second_greek)

# second_greek.sort()
# print(second_greek)

##########################################################

