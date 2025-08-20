def mostrar_matriz(matriz):
    """
    pre: recibe una matriz ya creada.
    pos: muestra por consola los elementos de la matriz.
    """
    nFilas = len(matriz)
    nColumnas = len(matriz[0])
    for fila in range(nFilas):
        for col in range(nColumnas):
            print("%3d" % matriz[fila][col], end="")
        print()
