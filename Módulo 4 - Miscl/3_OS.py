# import os
# # print(os.uname())     # Para Unix
# print(os.name)

# import platform
# print(platform.uname())

# Crear directorio en la carpeta actual de trabajo
# os.mkdir("my_first_directory")    #os.mkdir("./my_first_directory")
# print(os.listdir())

# Crear directorio en paralelo con la ruta actual de trabajo
# os.mkdir("../my_first_directory")
# print(os.listdir())

# Crear una carpeta dentro de otra
# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.listdir())

# Identificar directorio de trabajo actual
# os.chdir("my_first_directory")
# print(os.getcwd())
# os.chdir("my_second_directory")
# print(os.getcwd())

# Eliminar directorios (deben estar vacíos)
# os.makedirs("my_first_directory/my_second_directory")   # Para crear ruta de directorios
# print(os.listdir())
# os.rmdir("my_first_directory/my_second_directory")
# os.rmdir("my_first_directory")
# print(os.listdir())

# Eliminar direcgtorios (que NO están vacios)
# os.makedirs("my_first_directory/my_second_directory")
# os.removedirs("my_first_directory/my_second_directory")
# print(os.listdir())

############################################################################################
 ###############################--LAB 4.4.1.8: El módulo os--##############################
############################################################################################
# import os

# class BuscadorDirectorios:
    
#     def buscar(self, ruta, directorio):
#         print('Ejecutando búsqueda en', ruta)
#         try:
#             os.chdir(ruta)
#         except OSError:
#             # No procesa un archivo que no es un directorio.
#             return

#         directorio_actual = os.getcwd()
        
#         for entrada_actual in os.listdir("."):
#             if entrada_actual == directorio:
#                 print(os.getcwd() + "\\" + directorio)
                
#             # Llamada recursiva a find() para buscar en subdirectorios
#             self.buscar(directorio_actual + "\\" + entrada_actual, directorio)


# buscador_directorios = BuscadorDirectorios()
# buscador_directorios.buscar(".\\tree", "python")

###############--Solución EDUBE--#######################
import os

class DirectorySearcher:
    def find(self, path, dir):
        try:
            os.chdir(path)
        except OSError:
            # No procesa un archivo que no es un directorio.
            return

        current_dir = os.getcwd()
        for entry in os.listdir("."):
            if entry == dir:
                print(os.getcwd() + "\\" + dir)
            self.find(current_dir + "\\" + entry, dir)


directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")