print("Código ASCII:")

for caracter in range(32, 128, 16):

    print('\nCaracter:',end="")

    for codigo in range(caracter, caracter + 16):
      print('%4s'%chr(codigo), end="")
    print()

    print('Código:   ',end="")

    for codigo in range(caracter, caracter + 16):
      print('%4s'%codigo, end="")
    print()