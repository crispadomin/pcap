################################################
################################################

class MiPrimeraClase:
    pass

#######################--Tres objetos distintos, cada uno en una dirección de memoria--#########################
print()

objeto1 = MiPrimeraClase()
print(objeto1)

objeto2 = MiPrimeraClase()
print(objeto2)

objeto3 = MiPrimeraClase()
print(objeto3)

######################--Tres objetos distintos con el mismo nombre y distintas direcciones de memoria, se descartan los dos primeros--##########################
print()

objeto1 = MiPrimeraClase()
print(objeto1)

objeto1 = MiPrimeraClase()
print(objeto1)

objeto1 = MiPrimeraClase()
print(objeto1)

####################--Tres objetos distintos, con tres nombres distintos, referenciados a la misma direcciónd e memoria--############################
print()

objeto1 = MiPrimeraClase()
print(objeto1)

objeto2 = objeto1
print(objeto2)

objeto3 = objeto2
print(objeto3)