

def miLStrip(cadena, patron):
    while cadena[0] in patron:
        cadena = cadena[1:]
        if len(cadena) < 1:
            return ''
    return cadena
            
def miRStrip(cadena, patron):
    while cadena[-1] in patron:
        cadena = cadena[:-1]
        if len(cadena) < 1:
            return ''
    return cadena

def miStrip(cadena, patron):
    while cadena[0] in patron:
        cadena = cadena[1:]
        if len(cadena) < 1:
            return ''
    while cadena[-1] in patron:
        cadena = cadena[:-1]
        if len(cadena) < 1:
            return ''
    return cadena


#######################################

print(miLStrip("HHHola", "Hoa"))
print(miRStrip("Hoollaa", "la"))
print(miStrip("HHHHolaaaaa", "Halo"))

