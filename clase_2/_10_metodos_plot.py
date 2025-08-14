from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def plot_matriz(matriz):
    Z = np.array(matriz)  # conversión para graficar
    n, m = Z.shape
    x_vals = np.linspace(-3, 3, m)
    y_vals = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x_vals, y_vals)
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, edgecolor="k")  # simple y claro
    ax.set_title("Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Altura")
    plt.show()
