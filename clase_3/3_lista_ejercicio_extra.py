numeros = [0, 1, 2, 3, 4, 5]  # arreglo o iterable numeros
#cuadrados = []
cuadrados = list()
for num in numeros:
    #if num > 3:   si quiero puedo hacer esta condición primera forma
        #cuadrados.append(num) #si quiero puedo hacer esta condición primera forma
    # else:
    #    cuadrados.append(num**2) #si quiero puedo hacer esta condición primera forma   
    cuadrados.append(num**2)

print(cuadrados)

cuadrados_comp_1 = [num**2 for num in numeros] #cuadrados_comp = [num for num in numeros] eleva al cuadrado cada num en numeros, a todos, no tengo condición
                                            #[num**2 for num in numeros if num > 3] segunda forma con condición, el if va al final, si hay un else va antes del if
                                            #cuadrados_comp = [num**2 if num > 3 else num for num in numeros] tercera forma con condición if-else
cuadrados_comp_2 = [num**2 for num in numeros if num > 3] 
cuadrados_comp_3 = [num**2 if num > 3 else num for num in numeros] 
cuadrados_comp_4 = [num**2 if num**2 > 20 else num for num in numeros] #aca retorna el num cuando no cumple la condición, si cumple retorna el num al cuadrado

print(cuadrados_comp_1)
print(cuadrados_comp_2)
print(cuadrados_comp_3)
print(cuadrados_comp_4)

lst = [1,2,3]
lst.append(4)
lst.insert(2,5)  # inserta el 5 en la posición 2
lst.remove(2)  # elimina el primer 2 que encuentra
print(lst)
