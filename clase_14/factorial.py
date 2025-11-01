# Hagamos el Debug de la función factorial usando recursividad

def factorial_rec (n):
  if n == 0: # caso base
    return 1
  else:
    return n * factorial_rec(n-1) # caso recursivo
  

def factorial_ite (n):
    resultado = 1
    while n > 0:        # caso base
        resultado = resultado * n
        n-=1
    return resultado

# print(factorial(4))
# print(factorial_ite(4))

# -------------------------------------------------------
from functools import reduce
def suma_calificaciones(calificaciones):
   suma = reduce(lambda nota1, nota2 : nota1 + nota2, calificaciones)
   return suma


def sumar_lista(lista):
    if len(lista) == 0: # caso base/corte
        return 0 
    else:
        return lista[0] + sumar_lista(lista[1:]) # caso recursivo
    


calificaciones = [8, 7, 6.5, 8.5, 5, 9, 9.75]
suma = sumar_lista(calificaciones)
promedio = suma/len(calificaciones)
print(f"Nota promedio: {promedio:.2f}")





import time  # Importamos el módulo time

def cuenta_regresiva(n):
    if n == 0:
        print("Lift off!")
    else:
        print(n)
        time.sleep(1)  # Espera 1 segundo antes de continuar
        cuenta_regresiva(n - 1)

# cuenta_regresiva(5)