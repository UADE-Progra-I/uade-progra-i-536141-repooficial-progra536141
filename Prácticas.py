#  Ejercicio 2 (2 puntos)
"""
Implementá la función suma_matrices(A, B) que reciba dos matrices 
(listas de listas) de igual tamaño y devuelva la matriz suma.
Usar lista por comprension para inicializar la matriz suma
"""

print ("Respuesta Ejercicio 2")
def suma_matrices (a,b):
    fila = len(a)
    columna = len(a[0])
    
    C = [[0]* columna for fila in range (fila)]
    
    for i in range (fila):
        for j in range (columna):
            C[i][j] = A[i][j] + B[i][j]
    return C 
A = [[1,3], [3,5]] #dimension : 2x2
B = [[1,7], [4,8]] #dimension : 2x2

print (suma_matrices(A,B)) #deberia devolver [[2,10], [7,13]]

#######################################################################################################
"# Ejercicio 3 (1 punto)"
"Generá una lista por comprensión que contenga los cuadrados de los números pares entre 1 y 10."

print ("/n Respuesta Ejercicio 3")
cuadrados = [x**2 for x in range (11)]
print (cuadrados) 
#######################################################################################################
# Ejercicio 4 (1 punto)
"""
Lambda & Filter

Usando filter y lambda, quedate solo con los números positivos de una lista.
"""
print ("/n Respuesta Ejercicio 4")

numeros = [0,-1,1,-2,2,3,-3 ]
postivos = [ lambda numeros: 0>numeros]
print

"numeros = [1, -4, 5, -3, 2]"
"filtrados = list(filter(lambda x: x > 0, numeros))"
"print(filtrados)  # Debería imprimir [1, 5, 2]"
