import numpy as np
import matplotlib.pyplot as plt

# Creamos una matriz 5x5 con valores aleatorios (altura/densidad)
matriz = np.random.randint(1, 10, size=(50, 50))

print("Matriz de alturas/densidad:")
print(matriz)

# Graficar como mapa de calor
plt.imshow(matriz, cmap="viridis", origin="upper")
plt.colorbar(label="Altura / Densidad")

# Etiquetas y título
plt.title("Mapa de densidad (matriz 5x5)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar la gráfica
plt.show()
