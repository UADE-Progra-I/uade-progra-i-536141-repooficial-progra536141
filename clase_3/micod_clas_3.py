import math
# Ejemplo 3: Filtro con Condición if-else
# [ exp1 if condicion else exp2  for item in iterable]
lista = [1, -2, 5, 0, 3, 4]
listaPorComp = [num**2 if num % 2 == 0 else num for num in lista]
print("Cuadrados de pares, impares sin cambios:", listaPorComp)  # [1, 4, 5, 0, 3, 16]
