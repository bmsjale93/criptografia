from Crypto.Hash import HMAC, SHA256

def getHMAC(key_bytes,data_bytes):
    hmac256 = HMAC.new(key_bytes, msg=data_bytes, digestmod=SHA256)
    return hmac256.hexdigest()

def validateHMAC(key_bytes,data_bytes,hmac):
    hmac256 = HMAC.new(key_bytes,msg=data_bytes,digestmod=SHA256)
    result = "KO"
    try:
        hmac256.hexverify(hmac)
        result = "OK"
    except ValueError:
        result = "KO"
    print("¿Es válido?: " + result)
    return result

#Clave que se nos ha proporcionado
clave_bytes = bytes.fromhex('A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')

#Calculamos el HMAC-256
datos = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.", "utf8")
hmac = getHMAC(clave_bytes,datos)

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 53
textoTitulo = "-" * num_guiones1 + " EJERCICIO 6 " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

#Imprimimos el HMAC y si es válido el resultado
print("El HMAC calculado es:", hmac)
print(validateHMAC(clave_bytes, datos, hmac))
print()