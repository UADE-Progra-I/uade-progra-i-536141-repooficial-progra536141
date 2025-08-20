def rellenar_matriz(matriz):
    """
    pre: recibe una matriz ya creada.
    pos: llena la matriz con valores ingresados por el usuario.
    """
    # Detectar la cantidad de filas y columnas
    filas = len(matriz)
    columnas = len(matriz[0])
    for fil in range(filas):
        for col in range(columnas):
            num = int(input("Ingrese un número: "))
            matriz[fil][col] = num


def imprimir_matriz(matriz):
    """
    pre: recibe una matriz ya creada.
    pos: muestra por consola los elementos de la matriz.
    """

    filas = len(matriz)
    columnas = len(matriz[0])
    for fil in range(filas):
        for col in range(columnas):
            print("%3d" % matriz[fil][col], end="")
        print()


# Programa principal
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 4 filas y 3 columnas
rellenar_matriz(matriz)
imprimir_matriz(matriz)
