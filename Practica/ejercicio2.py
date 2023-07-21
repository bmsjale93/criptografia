from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

try:
    # Clave de cifrado
    key = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

    # Vector de inicialización (IV)
    iv = bytes.fromhex("00" * 16)

    # Texto cifrado
    ciphertext = base64.b64decode("TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=")

    # Crear un objeto AES cipher
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    # Descifrar el texto cifrado
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    #Imprimimos la clave por consola
    ancho = 50
    textoTitulo = "--------------------- EJERCICIO 1A ---------------------"
    textoSub = "Alejandro Delgado Martinez - 53344428E"

    #Personalizamos la impresión por consola
    ancho = 50
    num_guiones1 = 20
    num_guiones2 = 53
    textoTitulo = "-" * num_guiones1 + " EJERCICIO 2 " + "-" * num_guiones1
    textoSub = "Alejandro Delgado Martinez - 53344428E"
    print("\n" + textoTitulo.center(ancho))
    print(textoSub.center(ancho))
    print("-" * num_guiones2 + "\n")

    print("El texto descifrado es:", plaintext.decode())
    print()

except (ValueError, KeyError) as e:
    print("Error al descifrar el texto: ", str(e))
