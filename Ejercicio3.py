'''
CURSO ESPECIALIZACIÓN IA Y BIGDATA
PROGRAMACIÓN INTELIGENCIA ARTIFICIAL
UNIDAD 1
'''

def operar_conjuntos(lista1, lista2):

    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    resultado = {
        "interseccion": conjunto1 & conjunto2,
        "union": conjunto1 | conjunto2,
        "diferencia_simetrica": conjunto1 ^ conjunto2
    }

    return resultado


# Programa de prueba

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado = operar_conjuntos(lista1, lista2)

print("Intersección:", resultado["interseccion"])
print("Unión:", resultado["union"])
print("Diferencia simétrica:", resultado["diferencia_simetrica"])