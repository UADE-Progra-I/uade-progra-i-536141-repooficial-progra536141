from _3_metodos_crear import *
from _2_metodos_mostrar import mostrar_matriz


def matriz_por_escalar(matriz, escalar):
    nFilas = len(matriz)
    nColumnas = len(matriz[0])
    resultado = crear_matriz_nula(nFilas, nColumnas)
    for i in range(nFilas):
        for j in range(nColumnas):
            resultado[i][j] = matriz[i][j] * escalar
    return resultado


def matriz_por_matriz(matrizA, matrizB):
    # matriz 3x3 multiplica a matriz de 3x2 => resultado matriz 3x2
    # Condición: nColumnasA == nFilasB
    nFilasA = len(matrizA)
    nColumnasA = len(matrizA[0])
    nFilasB = len(matrizB)
    nColumnasB = len(matrizB[0])

    if nColumnasA != nFilasB:
        print("Solo se pueden multiplicar matrices cuando nColumnasA es igual a nFilasB")
        return None

    matriz_resultado = crear_matriz_nula(nFilasA, nColumnasB)

    for i in range(nFilasA):
        for j in range(nColumnasB):
            suma = 0
            for k in range(nFilasB):
                suma += matrizA[i][k] * matrizB[k][j]
            matriz_resultado[i][j] = suma

    return matriz_resultado


# Test Metodo
def test():
    matriz_A = [[1, 2, 3], [4, 5, 6]]
    matriz_B = [[1, 2], [3, 4], [5, 6]]
    escalar = 2
    matriz_1 = matriz_por_escalar(matriz_A, escalar)
    matriz_2 = matriz_por_matriz(matriz_A, matriz_B)
    print("\nMatriz A multiplicada por", escalar)
    mostrar_matriz(matriz_1)

    print("\nMatriz A multiplicada Matriz B")
    mostrar_matriz(matriz_2)


if __name__ == "__main__":
    test()
