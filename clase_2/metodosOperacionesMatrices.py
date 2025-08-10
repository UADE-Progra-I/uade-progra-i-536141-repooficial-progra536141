def mostrarMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(f"{columna}\t", end="")
        print()


def suma_matrices(A, B):
    filas = len(A)
    columnas = len(A[0])
    resultado = [[0] * columnas for i in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = A[i][j] + B[i][j]
    return resultado
