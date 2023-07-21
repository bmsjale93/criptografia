from psec import tr31

header, key = tr31.unwrap( kbpk = bytes.fromhex("A1A10101010101010101010101010102"), 
                           key_block = "D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B")

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 54
textoTitulo = "-" * num_guiones1 + " EJERCICIO 15 " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

#Imprimimos la clave en formato hexadecimal
print("Valor de la Clave:", key.hex())

#Imprimimos el resto
print("Key Version ID: " + header.version_id )
print("Algoritmo: " + header.algorithm)
print("Modo de uso: " + header.mode_of_use)
print("Uso de la clave: " + header.key_usage)
print("Exportabilidad: " + header.exportability)
print()