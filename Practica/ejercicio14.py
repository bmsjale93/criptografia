from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512

# Clave maestra proporcionada en el ejercicio
master_secret = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

# Identificador del dispositivo proporcionado en el ejercicio, que se utilizará como salt
salt = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")

# Usamos la función HKDF para derivar una nueva clave a partir de la clave maestra
# Usamos SHA-512 como algoritmo de hash y el identificador del dispositivo como salt
derived_key = HKDF(master_secret, 32, salt, SHA512)

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 54
textoTitulo = "-" * num_guiones1 + " EJERCICIO 14 " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

# Imprimimos la clave derivada en formato hexadecimal
print("Clave derivada:", derived_key.hex())
print()
