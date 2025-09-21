#actualizar producto

import csv

# newline: donde empieza la nueva linea
note = ''

with open('DB_CSV/produtos.csv', newline='') as produtos:

    #.reader: lo que hace es decir que voy a leer, como puse "as ->produtos<-"
    # estare leyendo el archivo por ese nombre

    #delimter= -> dicce que divide las columnas
    """data = csv.reader(produtos, delimiter=',') """
    
    # aprendi una manera de leer mi archivo csv de formatolista y pasar a diccionarrioa
    data = csv.DictReader(produtos,delimiter=',')
    #list() -> asigno la lista
    note = list(data)

# probando a que anda
# print(note)

def getData(note):

    # range(1,len(note)): -> empezamos del 2 posicion para sautar la cabecera
    """
    # comente porque ese funcionaba antes que pasara la lista
    # para el formatodde diccionario
    for i in range(1,len(note)): # marque el uno para que empiece a contar desde la primer posicion
        for j in range (len(note[i])): 
            # printo la cabezar separado por elementos
            print(note[0][j] + ": " + note[i][j])
        print('') # para hacer un salto de linea no mas y visualizar los datos separados
    """
    for producto in note:
        for key, value in producto.items(): # .items() leo claves e valores -> foi ciomo uma TUPLA
            print(key + ": " + value)
        print("")

def updateNombre(note, id_producto, nuevo_nombre):
    for producto in note:
        if producto["id"] == id_producto:
            producto["nombre"] = nuevo_nombre
            print("Producto del id: " + id_producto + "fue actualizado correctamente")
            return
    print("No existe un producto con ese id")

def updatePeso(note, id_producto, nuevo_peso):
    for producto in note:
        if producto["id"] == id_producto:
            producto["peso"] = nuevo_peso
            print("Producto del id: " + id_producto + "fue actualizado correctamente")
            return
    print("No existe un producto con ese id")

def updateEquivalencia(note, id_producto, nueva_equivalencia):
    for producto in note:
        if producto["id"] == id_producto:
            producto["equivalencia"] = nueva_equivalencia
            print("Producto del id: " + id_producto + "fue actualizado correctamente")
            return
    print("No existe un producto con ese id")

def updateEstoque(note, id_producto, actualizacion_estoque):
    for producto in note:
        if producto["id"] == id_producto:
            producto["estoque"] = actualizacion_estoque
            print("Producto del id: " + id_producto + "fue actualizado correctamente")
            return
    print("No existe un producto con ese id")

def updateCategoria(note, id_producto, nueva_categoria):
    for producto in note:
        if producto["id"] == id_producto:
            producto["categoria"] = nueva_categoria
            print("Producto del id: " + id_producto + "fue actualizado correctamente")
            return
    print("No existe un producto con ese id")

opcion = input("Elige una opcion para actualizar: nombre, peso, equivalencia, estoque o categoria: ")
match opcion: # para selecionar que vou usar
    case "nombre":
        id_producto = input("Ingrese el ID del produto ")
        print("")
        nuevo_nombre = input("Ingrese el nuevo Nombre ")
        updateNombre(note, id_producto, nuevo_nombre)

    case "peso":
        id_producto = input("Ingrese el ID del produto ")
        print("")
        nuevo_peso = input("Ingrese el nuevo Peso ")
        updatePeso(note, id_producto, nuevo_peso)

    case "equivalencia":
        id_producto = input("Ingrese el ID del produto ")
        print("")
        nueva_equivalencia = input("Ingrese el nuevo Equivalencia ")
        updateEquivalencia(note, id_producto, nueva_equivalencia)

    case "estoque":
        id_producto = input("Ingrese el ID del produto ")
        print("")
        actualizacion_estoque = input("Ingrese el nuevo valor de eslotque ")
        updateEstoque(note, id_producto, actualizacion_estoque)

    case "categoria":
        id_producto = input("Ingrese el ID del produto ")
        print("")
        nueva_categoria = input("Ingrese la nueva castegrioa ")
        updateCategoria(note, id_producto, nueva_categoria)

    case _: # para  ->_:<- para el caso inexistente ou seja o que nao esta alla
        print("Opcion imvalida")


# PREGUNTAS QUE TENGO PARA EL PROFE #
"""
1° -> porque no actualizo el csv? <- 
      preguntar al profe el jueves
"""
"""
2° -> se actualiza pero no guarda porque no se pasa los datos
      para el archivo csv
"""

# logre con ese video en a partir del time 16:00 -> https://www.youtube.com/watch?v=LYdsJ88e_ag

""" -> Guardar modificaciones en el .csv <- """
# 1° paso -> sacamos las keys de los campos

nombre_campos = ["id","nombre","peso","equivalencia_venta","categoria","id_provedor","estoque"]

""" fieldnames = note[0].keys() """
# -> mas avanzado, prefiero como hice arriba
# porque es mas facil de ver que es

with open('DB_CSV/produtos.csv', 'w', newline= '') as produtos:
    # 'w' -> modo escritura ->> para reescribir el archivo completamente
    writer = csv.DictWriter(produtos, fieldnames=nombre_campos)
    # me estaba dando error porque para el campo el identificados es 
    """ fieldnames"""
    writer.writeheader() # escribo aqui as linhas dos campos
    writer.writerows(note) # escribo aqui as filas de dados -> ou seja os valores dos campos

print("")
print("Los datos fueron actualizados en el archivo Produtps")

# para verificar si logre cambiar
getData(note) # leo de la memoria

# para leer del disco
# -> no entendi la diferencia pero vi en un video 
# -----> pregunta al profe cual la diferencia <----
"""
 with open('DB_CSV/produtos.csv', newline='') as disco:
    verif = list(csv.DictReader(disco))
getData(verif) 
"""

###########################################################################################################
