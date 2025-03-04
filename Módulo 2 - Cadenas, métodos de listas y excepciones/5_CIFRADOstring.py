#######################################################################################
#####################################---2.5.1.1/2---#####################################
#######################################################################################

# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)


# Cifrado César - descifrar un mensaje.
decipher =''
for char in cipher:
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    decipher += chr(code)
    
print(decipher)