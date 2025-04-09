import time

# Función para cifrar el mensaje
def cifrar_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for char in mensaje:
        if char.isalpha():  # Verificar si el carácter es una letra
            desplazado = chr(((ord(char.lower()) - 97 + desplazamiento) % 26) + 97)
            mensaje_cifrado += desplazado
        else:
            mensaje_cifrado += char  # No cifrar caracteres que no son letras
    return mensaje_cifrado

# Función para decifrar el mensaje
def decifrar_cesar(mensaje_cifrado, desplazamiento):
    mensaje_decifrado = ""
    for char in mensaje_cifrado:
        if char.isalpha():  # Verificar si el carácter es una letra
            desplazado = chr(((ord(char.lower()) - 97 - desplazamiento) % 26) + 97)
            mensaje_decifrado += desplazado
        else:
            mensaje_decifrado += char  # No decifrar caracteres que no son letras
    return mensaje_decifrado

# Mensaje a cifrar
mensaje = "lasallista"
desplazamiento = 7  # Desplazamiento en el cifrado César

# Cifrar el mensaje
mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
print("Mensaje Cifrado:", mensaje_cifrado)

# Simular un tiempo de espera para decodificar
print("\nEsperando para decifrar el mensaje...")
time.sleep(20)  # Pausa de 5 segundos antes de mostrar el mensaje decifrado

# Decifrar el mensaje
mensaje_decifrado = decifrar_cesar(mensaje_cifrado, desplazamiento)
print("Mensaje Decifrado:", mensaje_decifrado)
