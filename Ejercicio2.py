'''
CURSO ESPECIALIZACIÓN IA Y BIGDATA
PROGRAMACIÓN INTELIGENCIA ARTIFICIAL
UNIDAD 1
'''


import string
import unicodedata

def normalizar(texto):
    # Pasar a minúsculas
    texto = texto.lower()

    # Eliminar tildes
    texto = ''.join(
        caracter for caracter in unicodedata.normalize('NFD', texto)
        if unicodedata.category(caracter) != 'Mn'
    )

    # Eliminar signos de puntuación
    for signo in string.punctuation:
        texto = texto.replace(signo, '')

    return texto


def frecuencia_palabras(lista_palabras, ruta_fichero):

    # Crear diccionario
    frecuencias = {}

    for palabra in lista_palabras:
        frecuencias[normalizar(palabra)] = 0

    # Leer fichero
    with open(ruta_fichero, "r", encoding="utf-8") as fichero:
        texto = fichero.read()

    texto = normalizar(texto)

    # Dividir en palabras
    palabras_texto = texto.split()

    # Contar apariciones
    for palabra in palabras_texto:
        if palabra in frecuencias:
            frecuencias[palabra] += 1

    return frecuencias


# Programa de prueba
lista = ["python", "programacion", "gestion", "para"]

resultado = frecuencia_palabras(lista, "c:\\Dev\\ejercicio2.txt")

print("Frecuencia de palabras:")

for palabra in sorted(resultado):
    print(palabra, "->", resultado[palabra])