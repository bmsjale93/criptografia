import ed25519
import os

# Definimos la ruta de los archivos que contienen las claves
my_path = os.path.abspath(os.getcwd())
path_file_publ = my_path + "/Practica/ed25519-publ.pem"
path_file_priv = my_path + "/Practica/ed25519-priv.pem"

# Abrimos los archivos en modo lectura binaria y leemos las claves
publickey = open(path_file_publ,"rb").read()
privatekey = open(path_file_priv,"rb").read()

# Creamos la clave de firma a partir de la clave privada
signedKey = ed25519.SigningKey(privatekey)

# Definimos el mensaje que queremos firmar
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')

# Firmamos el mensaje con la clave de firma
signature = signedKey.sign(msg, encoding='hex')

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 55
textoTitulo = "-" * num_guiones1 + " EJERCICIO 13B " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

#Imprimimos la firma generada
print("Firma Generada (64 bytes):\n")
print(signature)


# Verificamos la firma
try:
    verifyKey = ed25519.VerifyingKey(publickey.hex(),encoding="hex")
    verifyKey.verify(signature, msg, encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")
