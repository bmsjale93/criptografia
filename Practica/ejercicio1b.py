#EJERCICIO 1a

#Definimos una función con los dos hexadecimales que utilizaremos
def xor_hex(hex1, hex2):
    
    # Convertir los números hexadecimales a enteros
    hex1_int = int(hex1, 16)
    hex2_int = int(hex2, 16)
    
    # Realizar la operación XOR
    xor_resultado = hex1_int ^ hex2_int
    
    # Convertir el resultado a hexadecimal
    xor_hex = format(xor_resultado, 'x')
    
    # Asegurarse de que el resultado tenga 16 bytes (32 caracteres hexadecimales)
    xor_hex = xor_hex.zfill(32)
    
    return xor_hex

# Clave fija en código
clave_fija = "B1EF2ACFE2BAEEFF"

# Clave dinámica en el archivo de propiedades
clave_dinamica = "B98A15BA31AEBB3F"

# Calcular la clave en memoria
clave_memoria = xor_hex(clave_fija, clave_dinamica)

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 54
textoTitulo = "-" * num_guiones1 + " EJERCICIO 1B " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

#Imprimimos la clave por consola
print("La clave con la que se trabaja en memoria es:", clave_memoria)
print()