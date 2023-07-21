from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

# Clave y nonce proporcionados
key = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce = base64.b64decode('9Yccn/f5nJJhAt2S')

# Texto a cifrar
data = "He descubierto el error y no volveré a hacerlo mal".encode()

# Crear el cifrador AES GCM
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

# Cifrar los datos
ciphertext, tag = cipher.encrypt_and_digest(data)

# Convertir a hexadecimal y base64
ciphertext_hex = ciphertext.hex()
ciphertext_b64 = base64.b64encode(ciphertext).decode('utf-8')

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 55
textoTitulo = "-" * num_guiones1 + " EJERCICIO 11B " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

#Imprimimos en Hexadecimal y en Base64
print("Texto cifrado en Hexadecimal: ", ciphertext_hex)
print("Texto Cifrado en Base64: ", ciphertext_b64)
print()