import numpy as np
import matplotlib.pyplot as plt
from math import exp, pi, sqrt


def crearMatrizNone(nFilas, nColumnas=None):
    if nColumnas is None:
        nColumnas = nFilas
    matriz = [[None] * nColumnas for _ in range(nFilas)]
    return matriz


def crearMatrizNula(nFilas, nColumnas=None):
    if nColumnas is None:
        nColumnas = nFilas
    matriz = [[0] * nColumnas for _ in range(nFilas)]
    return matriz


def crearMatrizNormal(nFilas, nColumnas=None):
    if nColumnas is None:
        nColumnas = nFilas
    matriz = crearMatrizNula(nFilas, nColumnas)

    # Parámetros de la normal
    mu_x, mu_y = 0, 0
    sigma_x, sigma_y = 1, 1

    # Rango de coordenadas
    x_vals = np.linspace(-3, 3, nColumnas)
    y_vals = np.linspace(-3, 3, nFilas)

    for i in range(nFilas):
        for j in range(nColumnas):
            x = x_vals[j]
            y = y_vals[i]
            # Fórmula de la normal bivariada
            z = (1 / (2 * pi * sigma_x * sigma_y)) * exp(
                -(((x - mu_x) ** 2) / (2 * sigma_x**2) + ((y - mu_y) ** 2) / (2 * sigma_y**2))
            )
            matriz[i][j] = z
    return matriz
