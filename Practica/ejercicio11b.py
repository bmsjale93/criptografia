from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import os

my_path = os.path.abspath(os.getcwd())
path_file_publ = my_path + "/Practica/clave-rsa-oaep-publ.pem"
path_file_priv = my_path + "/Practica/clave-rsa-oaep-priv.pem"

key_priv = RSA.importKey(open(path_file_priv).read())
key_publ = RSA.importKey(open(path_file_publ).read())


#Cifrado
msg = bytes(b'\xe2\xcf\xf8\x85\x90\x1aTI\xe9\xc4H\xba[\x94\x8a\x8cN\xe3w\x15+?\x1a\xcf\xa0\x14\x8f\xb3\xa4&\xdbr')
encryptor = PKCS1_OAEP.new(key_publ, SHA256)
encrypted = encryptor.encrypt(msg)

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 55
textoTitulo = "-" * num_guiones1 + " EJERCICIO 11B " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

#Imprimimos los datos cifrados
print("TEXTO CIFRADO:\n")
print(encrypted.hex())
print("--------------------------------------------------\n")