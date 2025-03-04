################################
# Lab 1
################################

# from os import strerror

# # Inicializa 26 contadores para cada letra latina.
# # Nota: hemos usado una comprensión para esto.
# counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# print(counters)

# file_name = input("Ingresa el nombre del archivo a analizar: ")
# try:
#     file = open(file_name, "rt")
#     for line in file:
#         for char in line:
#             # Si es una letra...
#             if char.isalpha():
#                 # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
#                 counters[char.lower()] += 1
#     file.close()
#     # Demos salida a los contadores.
#     for char in counters.keys():
#         c = counters[char]
#         if c > 0:
#             print(char, '->', c)
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno))
    
################################
# Lab 2
################################


# from os import strerror

# counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
# file_name = input("Ingresa el nombre del archivo a analizar: ")
# try:
#     file = open(file_name, "rt")
#     for line in file:
#         for char in line:
#             if char.isalpha():
#                 counters[char.lower()] += 1
#     file.close()
#     file = open(file_name + '.hist', 'wt')
#     # Nota: hemos utilizado una lambda para acceder a los elementos del directorio y se ha establecido reverse a True para obtener un orden válido.
#     for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
#         c = counters[char]
#         if c > 0:
#             file.write(char + ' -> ' + str(c) + '\n')
#     file.close()
# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno))

################################
# Lab 3
################################

# # Una clase de la excepción base para nuestro código:
# class StudentsDataException(Exception):
#     pass


# # Una excepción para líneas erróneas:
# class WrongLine(StudentsDataException):
#     def __init__(self, line_number, line_string):
#         super().__init__(self)
#         self.line_number = line_number
#         self.line_string = line_string


# # Una excepción para un archivo vacío.
# class FileEmpty(StudentsDataException):
#     def __init__(self):
#         super().__init__(self)


# from os import strerror

# # Un diccionario para los datos de los estudiantes:
# data = { }

# file_name = input("Ingresa el nombre del archivo de datos del estudiante: ")
# line_number = 1
# try:
#     f = open(file_name, "rt")
#     # Leer el archivo completo en la lista.
#     lines = f.readlines()
#     f.close()
#     # ¿El archivo está vacío?
#     if len(lines) == 0:
#         raise FileEmpty()
#     # Escanee el archivo línea por línea.
#     for i in range(len(lines)):
#         # Obtener la línea n.
#         line = lines[i]
#         # Divídirlo en columnas.
#         columns = line.split()
#         # Debe haber 3 columnas, ¿están ahí?
#         if len(columns) != 3:
#             raise WrongLine(i + 1, line)
#         # Construye una clave a partir del nombre y apellido del estudiante.
#         student = columns[0] + ' ' + columns[1]
#         # Obtener puntos.
#         try:
#             points = float(columns[2])
#         except ValueError:
#             raise WrongLine(i + 1, line)
#         # Actualizar diccionario.
#         try:
#             data[student] += points
#         except KeyError:
#             data[student] = points
#     # Imprimir resultados.
#     for student in sorted(data.keys()):
#         print(student,'\t', data[student])

# except IOError as e:
#     print("Se produjo un error de E/S: ", strerror(e.errno))
# except WrongLine as e:
#     print("Línea incorrecta #" + str(e.line_number) + " en el archivo fuente:" + e.line_string)
# except FileEmpty:
#     print("Archivo fuente vacío")

####################
# Lab 1 Jose Antonio
####################

###################
# def obtener_diccionario():
#     try:
#         contar_letras = {}
#         ruta_archivo = 'text.txt' #input('ingresa la ruta de un archivo')
#         fichero = open(ruta_archivo, 'rt', encoding='utf-8')
#         for caracter in fichero.readline():
#             if caracter.isalpha():
#                 if caracter.upper() in contar_letras:
#                     contar_letras[caracter.upper()] += 1
#                 else:
#                     contar_letras[caracter.upper()] = 1
#         return contar_letras
#     except:
#         print('No se ha podido realizar la operacion')


# def histograma(diccionario: dict):
#     for clave, valor in sorted(diccionario.items()):
#         print(clave, '*'*valor)


# histograma(obtener_diccionario())

#########################
# Lab 1 Alba
#########################

# from os import strerror

# try:
#     counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
#     file = input("Introduce el nombre del archivo: ")
#     stream = open(file, "rt")
#     while True:
#         char = stream.read(1).lower()
#         if not char:
#             break
        
#         if char in counters.keys():
#             counters[char] += 1
#     stream.close()
#     print("Caracteres en el archivo:")
#     for clave, valor in counters.items():
#         if valor == 0:
#             continue
#         else:
#             print("\t"+clave+": "+str(valor))
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))


##########################
# Lab2 Jose Antonio
##########################

# def obtener_diccionario():
#     try:
#         contar_letras = {}
#         ruta_archivo = 'text.txt' #input('ingresa la ruta de un archivo')
#         fichero = open(ruta_archivo, 'rt', encoding='utf-8')
#         for caracter in fichero.readline():
#             if caracter.isalpha():
#                 if caracter.upper() in contar_letras:
#                     contar_letras[caracter.upper()] += 1
#                 else:
#                     contar_letras[caracter.upper()] = 1
#         return contar_letras
#     except:
#         print('No se ha podido realizar la operacion')

# def histograma(diccionario: dict, clave=lambda x: x):
#     for clave, valor in sorted(diccionario.items(), key=clave):
#         print(clave, '*'*valor)

# def grabar(contenido, nombre):
#     try:
#         archivo = open(nombre, 'w')
#         for clave, valor in contenido.items():
#             txt = clave +' : ' + '*'*valor +'\n'
#             archivo.write(txt)
      
#     except Exception as e:
#         print(e)
#         print('No se ha podido realizar la operacion')

# histograma(obtener_diccionario())
# print()
# histograma(obtener_diccionario(), clave=lambda x: x[1])
# grabar(obtener_diccionario(), 'histograma.hist')


#####################
# Lab 2 Cristina
#####################


# from os import strerror
# counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
# source_file_name = input("Ingresa el nombre del archivo fuente: ")
# try:
#     source_file = open(source_file_name, 'rt')
#     ch = source_file.read(1)
#     while ch.isalpha and ch != '':
#         if ch.lower() in counters.keys():
#             counters[ch.lower()] += 1
#         ch = source_file.read(1)
# except IOError as e:
#     print("No se puede abrir archivo fuente: ", strerror(e.errno))
#     exit(e.errno) 
    
# source_file.close()
# sorted_counters = dict(sorted(counters.items(), key=lambda x: x[1], reverse=True))
# for ch, val in sorted_counters.items():
#     if sorted_counters[ch] != 0:
#         print(ch, '->', val)


#################################
# Lab 3 Jose Antonio
#################################
from os import strerror

# def leer_archivo(ruta='jekyll.txt') -> dict:
#     alumnos_nota = {}
#     try:
#         archivo = open(ruta, 'r')
#         for linea in archivo.readlines():
#             nombre, apellido, nota = linea.replace('\n','').split(' ')
#             if nombre + ' ' + apellido in alumnos_nota:
#                 alumnos_nota[nombre + ' ' + apellido] += float(nota)
#             else:
#                 alumnos_nota[nombre + ' ' + apellido] = float(nota)
#         return alumnos_nota
#     except IOError as e:
#         print('Se ha producido un error', strerror(e.errno))

# def imprimir_notas(notas:dict):
#     for nombre, nota in notas.items():
#         print(nombre, ':', nota)

# imprimir_notas(leer_archivo())


#################################
# Ramón lab2
#################################

# from os import  strerror
# import string
# source_file_name = input("Ingresa el nombre del archivo fuente: ")
# try:
#     abecedario = {}
#     source_file = open(source_file_name, "r", encoding = "utf-8")
#     content = source_file.read()
#     source_file.close()
#     for char in content:
#         letra = char.lower()
#         letra_formateada = letra
#         if letra == 'á': letra_formateada = "a"
#         if letra == 'é': letra_formateada = "e"
#         if letra == 'í': letra_formateada = "i"
#         if letra == 'ó': letra_formateada = "o"
#         if letra == 'ú': letra_formateada = "u"
#         if letra_formateada in abecedario:
#             abecedario[letra_formateada] += 1
#         else:
#             abecedario[letra_formateada] = 1
    
#     lista_ordenada_alfabeticamente = sorted(abecedario.keys())
#     lista_ordenada_cantidad = sorted(abecedario.items(), key=lambda item:item[1], reverse=True)
    
    
#     print("Caracteres sin ordenar: ", end="\t"*2)
#     for key, value in abecedario.items():
#         if key in list(string.ascii_lowercase):
#             print(f"{key}: {value}", end=" | ")
#     print()
#     print("Caracteres ordenados alfabéticamente: ", end="\t")
#     for key in lista_ordenada_alfabeticamente:
#         if key in list(string.ascii_lowercase):
#             print(f"{key}: {abecedario[key]}", end=" | ")
#     print()
#     print("Caracteres ordenados por valor: ", end="\t")
#     for key, value in lista_ordenada_cantidad:
#         if key in list(string.ascii_lowercase):
#             print(f"{key}: {value}", end=" | ")
#     print()
#     print("Todos los caracteres: ", end="\t"*3)
#     for key, value in abecedario.items():
#         if key == '\n':
#             new_key = '\\n'
#             print(f"{new_key}: {value}", end=" | ")
#         else:
#             print(f"{key}: {value}", end=" | ")
# except IOError as e:
#     print("No se puede abrir el archivo fuente: ", strerror(e.errno))
#     exit(e.errno)