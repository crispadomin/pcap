##############################################################################
##################-ERRORES EN EL PROCESAMIENTO DE ARCHIVOS--##################
##############################################################################

# import errno

# try:
#     s = open("c:/users/user/Desktop/file.txt", "rt")
#     # El procesamiento va aquí.
#     s.close()
# except Exception as exc:
#     if exc.errno == errno.ENOENT:
#         print("El archivo no existe.")
#     elif exc.errno == errno.EMFILE:
#         print("Demasiados archivos abiertos.")
#     else:
#         print("El numero del error es:", exc.errno)

##################-Otra forma de procesar errores de archivos--##################

# from os import strerror

# try:
#     s = open("c:/users/user/Desktop/file.txt", "rt")
#     # El procesamiento va aquí.
#     s.close()
# except Exception as exc:
#     print("El archivo no pudo ser abierto:", strerror(exc.errno))

##############################################################################
 ##################--OPERACIONES DE LECTURA DE ARCHIVOS--##################
##############################################################################

# from os import strerror

# # Para conocer el tamaño del archivo antes de abrirlo
# import os
# print(os.path.getsize("text.txt"), 'bytes')

# try:
#     counter = 0
#     stream = open('text.txt', "rt")     # Abrir en modo 'leer texto'
#     char = stream.read(1)               # Leer caracteres uno a uno
#     # content = stream.read()           # Leer el archivo completo
#     # line = stream.readline()          # Leer líneas una a una
#     # lines = stream.readlines(3)         # Leer un máximo de 3 líneas del archivo: devuelve una lista
#     lines = stream.readlines()          #Leer todas las líneas del archivo: devuelve todas la líenas en una lista.
#     while char != '':
#         print(char, end='')
#         counter += 1
#         char = stream.read(1)
#     stream.close()
#     print("\n\nCaracteres en el archivo:", counter)
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

      ##################--OTRA FORMA DE LECTURA DE ARCHIVOS--##################
	
# from os import strerror

# try:
# 	character_counter = line_counter = 0
# 	for line in open('text.txt', 'rt'):         # No es necesario cerrar el archivo, se cierra automáticamente
# 		line_counter += 1
# 		for char in line:
# 			print(char, end='')
# 			character_counter += 1
# 	print("\n\nCaracteres en el archivo: ", character_counter)
# 	print("Líneas en el archivo:     ", line_counter)
# except IOError as e:
# 	print("Se produjo un error de E/S:", strerror(e.errno))

##############################################################################
 ##################--OPERACIONES DE ESCRITURA DE ARCHIVOS--##################
##############################################################################

# from os import strerror

# try:
# 	file = open('newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
# 	for i in range(10):
# 		s = "línea #" + str(i+1) + "\n"
# 		for char in s:
# 			file.write(char)
# 	file.close()
# except IOError as e:
# 	print("Se produjo un error de E/S:", strerror(e.errno))

##############################################################################
            ##################--BYTEARRAY()--##################
##############################################################################
# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 100 - i

# print()

# for b in data:
#     print('binario:', bin(b), end = ' - ')
#     print('hexadecimal:', hex(b), end = ' - ')
#     print('octal:', oct(b), end = ' - ')
#     print('decimal:', int(b))

##############################################################################
            ##################--ARCHIVO BINARIO--##################
##############################################################################
# from os import strerror

# data = bytearray(10)

# for i in range(len(data)):
#     data[i] = 10 + i

# try:
#     binary_file = open('file.bin', 'wb')
#     binary_file.write(data)
#     binary_file.close()
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

# ############################################

# from os import strerror

# data = bytearray(10)

# try:
#     binary_file = open('file.bin', 'rb')
#     binary_file.readinto(data)
#     binary_file.close()

#     for b in data:
#         print(hex(b), end=' ')
# except IOError as e:
#     print("Se produjo un error de E/S:", strerror(e.errno))

#################################################################################################
  ##################--LAB 4.3.1.15: Histograma de frecuencia de caracteres--##################
#################################################################################################

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
# for ch, val in counters.items():
#     if counters[ch] != 0:
#         print(ch, '->', val)

#################################################################################################
  ##############--LAB 4.3.1.16: Histograma de frecuencia de caracteres ordenado--##############
#################################################################################################

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

#################################################################################################
  ##############--LAB 4.3.1.17: Evaluando los resultados de los estudiantes--##############
#################################################################################################
from os import strerror

# alumno_puntos = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
source_file_name = input("Ingresa el nombre del archivo fuente: ")

source_file = open(source_file_name, 'rt')
lines = source_file.readlines()
students = {}

for student in range(len(lines)):
    line = lines[student].split()
    key = line[0] + '\t' + line[1]
    value = float(line[2])
    if key in students.keys():
        students[key] += value
    else:
        students [key] = value

print(students)

file = open('newtext.txt', 'wt')

for key in students.keys():
    new_line = key + '\t' + str(students[key]) + '\n'
    file.write(new_line)

file.close()

source_file.close()
# class StudentsDataException(Exception):
#     pass


# class WrongLine(StudentsDataException):
#     # Escribe tu código aquí.


# class FileEmpty(StudentsDataException):
#     # Escribe tu código aquí.