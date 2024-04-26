import re  # Importar expresiones regulares

nombre_archivo = "ejemplo.json"
caracteres_unicode = []
palabras = []
errores = []
meses_con_30_dias = [4, 6, 9, 11]  # Abril, Junio, Septiembre, Noviembre
meses_con_31_dias = [1, 3, 5, 7, 8, 10, 12] # Enero, Marzo, Mayo, Julio, Agosto, Octubre, Dicimebre
try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()  # Leer todo el contenido del archivo

        i = 0
        while i < len(contenido):
            caracter = contenido[i]

            # Agregar cada caracter a la lista de Unicode siempre
            caracteres_unicode.append((caracter, ord(caracter)))

            # Detectar inicio de palabra entre comillas
            if caracter == '"':
                palabra = ""
                i += 1  # Mover al siguiente caracter
                while i < len(contenido) and contenido[i] != '"':
                    palabra += contenido[i]
                    caracteres_unicode.append((contenido[i], ord(contenido[i])))  # Agregar también estos caracteres
                    i += 1
                if i >= len(contenido):  # Comprobar cierre de comillas
                    print("Error: No se encontró la comilla de cierre.")
                    break
                palabras.append((palabra, 777))
            elif caracter.isdigit() or (caracter == '.' and i + 1 < len(contenido) and contenido[i + 1].isdigit()):
                # Leer número completo
                num_start = i
                num = ''
                if caracter == '.':
                    num = '0'  # Prepend '0' if starts with '.'
                while i < len(contenido) and (contenido[i].isdigit() or contenido[i] == '.'):
                    num += contenido[i]
                    i += 1
                if num.endswith('.'):  # Error si el número termina en punto
                    errores.append((num, "Error: número termina con punto."))
                elif num.startswith('0') and len(num) > 1 and num[1] != '.':
                    errores.append((num, "Error: número con cero no significativo."))
                continue  # Evitar incrementar 'i' nuevamente

            # Detección de fechas en formato dd/mm/aa
            if re.match(r'(\d{2})/(\d{2})/(\d{2})', contenido[i:i + 8]):
                fecha = contenido[i:i + 8]
                dia, mes, ano = map(int, fecha.split('/'))
                if mes == 2 and dia > 29:  # Febrero y días
                    errores.append((fecha, "Error: Febrero no tiene más de 29 días."))
                elif mes in meses_con_31_dias and dia > 31:
                    errores.append((fecha, "Error: Este mes no tiene más de 31 días."))
                elif mes in meses_con_30_dias and dia > 30:
                    errores.append((fecha, "Error: Este mes no tiene más de 30 días."))
                i += 7  # Avanzar índice más allá de la fecha procesada

            i += 1  # Mover al siguiente caracter

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

# Imprimir errores detectados en números y fechas sólo si hay errores
if errores:
    print("Errores encontrados:")
    for error in errores:
        print(f"{error[0]} {error[1]}")
