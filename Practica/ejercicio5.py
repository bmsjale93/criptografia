import hashlib

# Texto en claro
plaintext = "En KeepCoding aprendemos cómo protegernos con criptografía."

# Crear un objeto SHA3-256
hash_object = hashlib.sha3_256()

# Actualizar el objeto hash con el texto en claro codificado
hash_object.update(plaintext.encode())

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 53
textoTitulo = "-" * num_guiones1 + " EJERCICIO 5 " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

# Imprimir el hash en hexadecimal
print("El hash SHA3-256 del texto es:", hash_object.hexdigest())
