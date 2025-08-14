import random
from _2_metodos_mostrar import mostrar_matriz


def crear_matriz_nula(nFilas, nColumnas):
    """
    pre: recibe numero de nFilas y numero de nColumnas
    pos: devuelve una matriz nuala de filasxcolumnas creada con ceros
    """
    return [[0] * nColumnas for _ in range(nFilas)]


def crear_matriz_random(nFilas, nColumnas):
    """
    pre: recibe numero de filas y numero de columnas
    pos: retorna una matriz con valores aleatorios entre 1 y 10
    """
    matriz_random = []
    for fila in range(nFilas):
        fila_actual = []
        for col in range(nColumnas):
            num_aleatorio = random.randint(1, 10)
            fila_actual.append(num_aleatorio)
        matriz_random.append(fila_actual)
    return matriz_random


# Test metodos
def test():
    # Creamos una matriz nula de 2x3
    matriz_nula = crear_matriz_nula(2, 3)
    print("\nMatriz nula de 2x3")
    mostrar_matriz(matriz_nula)

    # Creamos una matriz random de 2x3
    matriz_random = crear_matriz_random(2, 3)
    print("\nMatriz nula de 2x3")
    mostrar_matriz(matriz_random)

    help(crear_matriz_nula)


if __name__ == "__main__":
    test()
