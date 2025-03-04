class ValorFueraRango(Exception):
    pass

def read_int(prompt, min, max):
    otra_vez = 1
    while otra_vez == 1:
        try:
            value =  int(input(prompt))
            if value > min and value < max:
                return value
                otra_vez = 0
            else:
                raise ValorFueraRango
        except ValueError:
            print ("Error: entrada incorrecta.")
        except ValorFueraRango:
            print("Error: el valor no está dentro del rango permitido (min..max).")
        except Exception as ex:         #Para conocer información sobre la expección capturada
            print("\tExcepción:", type(ex).__name__)
            print('\t',ex)


v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)
print("El número es:", v)