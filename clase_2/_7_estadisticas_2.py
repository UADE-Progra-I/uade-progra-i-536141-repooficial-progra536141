def procesar_matriz(matriz):
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

    return suma_total, promedio, suma_filas, suma_columnas


def imprimir_resultados(suma_total, promedio, suma_filas, suma_columnas):
    print("Suma total de los elementos de la matriz:", suma_total)
    print("Promedio de los elementos de la matriz:", promedio)
    print("Suma de cada fila:")
    for i in range(len(suma_filas)):
        print("Fila", i, "=", suma_filas[i])
    print("Suma de cada columna:")
    for j in range(len(suma_columnas)):
        print("Columna", j, "=", suma_columnas[j])


# Test Metodos
def test():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    suma_total, promedio, suma_filas, suma_columnas = procesar_matriz(matriz)
    imprimir_resultados(suma_total, promedio, suma_filas, suma_columnas)


if __name__ == "__main__":
    test()
