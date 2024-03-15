nombre_archivo = "ejemplo.json"
caracteres_unicode = []
palabras = []

try:
    with open(nombre_archivo, "r") as archivo:
        caracter = archivo.read(1)
        while caracter:
            caracteres_unicode.append((caracter, ord(caracter)))  # Agregar carácter y su código Unicode a la lista
            caracter = archivo.read(1)


except FileNotFoundError:
    print("El archivo no se encontró.")
except IOError:
    print("Error al leer el archivo.")

try:
    with open(nombre_archivo, "r") as archivo:
        caracter = archivo.read(1)
        while caracter:
            caracter = archivo.read(1)

            # Detectar inicio de palabra entre comillas
            if caracter == '"':
                palabra = ""
                caracter = archivo.read(1)  # Leer siguiente carácter
                # Leer caracteres hasta encontrar la siguiente comilla
                while caracter != '"':
                    if caracter == '':
                        print("Error: El archivo JSON tiene un error. No se encontró la comilla de cierre.")
                        break
                    if caracter.isalpha():  # Verificar si el caracter es una letra
                        palabra += caracter
                    caracter = archivo.read(1)
                else:
                    # Agregar la palabra y su token 777 a la lista de palabras
                    palabras.append((palabra, 777))

except FileNotFoundError:
    print("El archivo no se encontró.")
except IOError:
    print("Error al leer el archivo.")


# Imprimir la lista de caracteres con sus códigos Unicode
for caracter, unicode in caracteres_unicode:
    print(f"Carácter: {caracter} - Token: {unicode}")

print("--------------------------")

# Imprimir la lista de palabras con su token 777
print("Lista de palabras:")
for palabra, token in palabras:
    print(f"Palabra: {palabra} - Token: {token}")
