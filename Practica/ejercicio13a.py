# Importamos las bibliotecas necesarias
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import binascii
import os

# Obtenemos la ruta absoluta del directorio actual
my_path = os.path.abspath(os.getcwd())

# Construimos la ruta completa al archivo de la clave privada
path_file_priv = my_path + "/Practica/clave-rsa-oaep-priv.pem"

# Importamos la clave privada desde el archivo
key = RSA.importKey(open(path_file_priv).read())

# Definimos el mensaje que queremos firmar
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')

# Creamos un hash del mensaje usando SHA256
hash = SHA256.new(msg)

# Creamos un objeto firmante usando nuestra clave privada
signer = PKCS115_SigScheme(key)

# Firmamos el hash del mensaje
signature = signer.sign(hash)

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 55
textoTitulo = "-" * num_guiones1 + " EJERCICIO 13A " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

# Imprimimos la firma en formato hexadecimal
print("Firma:\n")
print(signature.hex())
print()