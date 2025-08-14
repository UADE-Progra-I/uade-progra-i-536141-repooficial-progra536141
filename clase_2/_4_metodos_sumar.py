from _3_metodos_crear import *


def sumar_matrices(matrizA, matrizB):
    # Para sumar matrices deben tener la misma longitud
    if len(matrizA) != len(matrizB) or len(matrizA[0]) != len(matrizB[0]):
        print("Imposible sumar matrices de diferente dimensión")
        return
    nFilas = len(matrizA)
    nColumnas = len(matrizA[0])
    resultado = crear_matriz_nula(nFilas, nColumnas)
    for i in range(nFilas):
        for j in range(nColumnas):
            resultado[i][j] = matrizA[i][j] + matrizB[i][j]
    return resultado


# Test metodos
def test():
    matriz_A = [[1, 2], [3, 4]]
    matriz_B = [[5, 6], [7, 8]]
    matriz_C = sumar_matrices(matriz_A, matriz_B)
    print("Suma de matrices A y B:", matriz_C)


if __name__ == "__main__":
    test()
