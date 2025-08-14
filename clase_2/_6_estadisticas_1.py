def estadisticas_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    suma_total = 0
    suma_filas = [0] * filas
    suma_columnas = [0] * columnas

    # Calcular la suma total, suma de filas y suma de columnas
    for i in range(filas):
        for j in range(columnas):
            suma_total += matriz[i][j]
            suma_filas[i] += matriz[i][j]
            suma_columnas[j] += matriz[i][j]

    # Calcular el promedio
    total_elementos = filas * columnas
    promedio = suma_total / total_elementos

    print("Total:", suma_total)
    print("Promedio:", promedio)
    print("Suma de cada fila:", suma_filas)
    print("Suma de cada columna:", suma_columnas)


# Test Metodos
def test():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matriz)
    estadisticas_matriz(matriz)


if __name__ == "__main__":
    test()
