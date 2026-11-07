'''
CURSO ESPECIALIZACIÓN IA Y BIGDATA
PROGRAMACIÓN INTELIGENCIA ARTIFICIAL
UNIDAD 1

Creamos la lista 'datos' con los números y lo pasamos por parámetro a procesar_lista (lista)

'''

def procesar_lista(lista):
    # 1. Eliminar negativos. Recorre lista y sólo almacena lo que sean positivos
    positivos = [n for n in lista if n >= 0]

    # 2. Eliminar repetidos. Creamos un conjunto de positivos. Los conjuntos no admiten repetidos. List convierte el conjunto en lista
    sin_repetidos = list(set(positivos))

    # 3. Ordenar de menor a mayor, meidante sort
    sin_repetidos.sort()

    # devuelve sin_repetidos con la lista con los requisitos
    return sin_repetidos


# Ejemplo de uso
datos = [4, -1, 2, 4, 3, -5, 2]
#pasamos la lista y la devuelve en resultado
resultado = procesar_lista(datos)

# muestra el resultado
print(resultado)