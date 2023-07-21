import jwt

# JWT
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI"

# Clave secreta
key = "Con KeepCoding aprendemos"

try:
    # Decodificar el JWT
    decoded = jwt.decode(token, key, algorithms=["HS256"])

    # Imprimir la cabecera y el cuerpo
    print("Cabecera:", jwt.get_unverified_header(token))
    print("Cuerpo:", decoded)

except jwt.InvalidTokenError:
    
    #Personalizamos la impresión por consola
    ancho = 50
    num_guiones1 = 20
    num_guiones2 = 54
    textoTitulo = "-" * num_guiones1 + " EJERCICIO 4B " + "-" * num_guiones1
    textoSub = "Alejandro Delgado Martinez - 53344428E"
    print("\n" + textoTitulo.center(ancho))
    print(textoSub.center(ancho))
    print("-" * num_guiones2 + "\n")
    
    print("El JWT es inválido.")
    print()