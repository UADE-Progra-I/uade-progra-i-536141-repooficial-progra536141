import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Matriz 5x5
matriz1 = np.random.randint(1, 10, size=(10, 10))
matriz2 = np.random.randint(1, 10, size=(50, 50))

print("Matriz de alturas/densidad:")
# print(matriz1)

# Graficar con heatmap
sns.heatmap(matriz1, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={"label": "Altura / Densidad"})
sns.heatmap(matriz2, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={"label": "Altura / Densidad"})

plt.title("Mapa de densidad (Seaborn)")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
