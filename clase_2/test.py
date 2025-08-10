def mostrar_matriz(m):
    for fila in m:
        print(fila)


# filas = [0] * 3
# print(filas)

filas = 3
columnas = 2
matriz = [[0] * 2 for columna in range(filas)]
mostrar_matriz(matriz)
