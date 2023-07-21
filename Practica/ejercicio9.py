from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# Clave AES
key = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

#Personalizamos la impresión por consola
ancho = 50
num_guiones1 = 20
num_guiones2 = 53
textoTitulo = "-" * num_guiones1 + " EJERCICIO 9 " + "-" * num_guiones1
textoSub = "Alejandro Delgado Martinez - 53344428E"
print("\n" + textoTitulo.center(ancho))
print(textoSub.center(ancho))
print("-" * num_guiones2 + "\n")

# Calcular el KCV(SHA-256)
hash_object = SHA256.new()
hash_object.update(key)
kcv_sha256 = hash_object.digest()[:3]
print("KCV(SHA-256):", kcv_sha256.hex())

# Calcular el KCV(AES)
cipher = AES.new(key, AES.MODE_ECB)
plaintext = bytes(16)  # 16 bytes de ceros
ciphertext = cipher.encrypt(plaintext)
kcv_aes = ciphertext[:3]
print("KCV(AES):", kcv_aes.hex())
print()