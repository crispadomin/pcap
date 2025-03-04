# Imprimir los primeros 10000 caracteres unicode

for i in range(0,10000):
    print('\\u' + str(i), "- Caracter:", chr(i))

#Código UNICODE al que corresponde la letra 'a'
print(ord("a"))