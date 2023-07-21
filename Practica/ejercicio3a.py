from Crypto.Cipher import ChaCha20
import base64

# Clave de cifrado
clave = bytes.fromhex("AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120")

# Nonce
nonce = base64.b64decode("9Yccn/f5nJJhAt2S")

# Texto en claro
texto = "KeepCoding te enseña a codificar y a cifrar"

# Crear un objeto ChaCha20 cipher
cifrado = ChaCha20.new(key=clave, nonce=nonce)

# Cifrar el texto en claro
textoCifrado = cifrado.encrypt(texto.encode())

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 54
textoTitulo = "-" * num_guiones1 + " EJERCICIO 3A " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

print("El texto cifrado es:", base64.b64encode(textoCifrado).decode())
print()