
# Ejercicio 1
"""
Desarrollar la función write_productos()
que guarde una lista de listas en el archivo productos.csv del directorio data 
con formato csv.

🔹 La función recibe como argumento una lista con los productos a persistir.
🔹 La función persiste los datos en el archivo productos.csv.
🔹 Debe validar que la lista de productos no esté vacía ni sea de tipo incorrecto.
🔹 Si la validación falla, debe generar una excepción.
🔹 Abrir el archivo en modo escritura ("w").
🔹 Usar csv.writer() y el método writerows(data).

Ejemplo de estructura esperada:
productos = [
    [1, "Remera Azul", "Indumentaria", 9500.50],
    [2, "Pantalón Negro", "Indumentaria", 13500.00]
]
"""

# Ejercicio 2

"""
Desarrollar la función read_productos()
que retorne el contenido del archivo productos.csv del directorio data
en forma de lista de listas.

🔹 Abrir el archivo en modo lectura ("r").
🔹 Leer su contenido usando el módulo csv.
🔹 Retornar una lista de listas con los registros.
🔹 Manejar el caso en que el archivo no exista (FileNotFoundError) devolviendo una lista vacía.

"""

# Ejercicio 3
"""
A partir de la siguiente lista de productos base:

productos = [
    [1, "Remera Azul", "Indumentaria", 9500.50],
    [2, "Pantalón Negro", "Indumentaria", 13500.00],
    [3, "Campera de Jean", "Indumentaria", 23000.00]
]

Desarrollar la función inicializar_productos()
que cree el archivo productos.csv y lo inicialice con esta lista modelo.

🔹 Utilizar internamente la función write_productos() para persistir los datos.
🔹 Si el archivo ya existe, debe sobrescribirse.
"""

# Ejercicio 4
"""
Desarrollar la función insert_productos()
que recibe una lista con los datos de un solo producto y lo inserta al final del archivo productos.csv.

🔹 Abrir el archivo productos.csv en modo "a" (append).
🔹 Usar csv.writer() y el método writerow(producto).
🔹 Validar que el producto sea una lista no vacía y con 4 campos.
🔹 Si el archivo no existe, mostrar un mensaje de error o llamar a inicializar_productos().
"""

# Ejercicio 5
"""
Desarrollar la función input_productos()
que lea por consola los datos de un nuevo producto y los almacene en una lista.

🔹 Solicitar al usuario: nombre_producto, categoría y precio_unitario.
🔹 Calcular el id automáticamente leyendo el último registro del archivo.
🔹 Validar los datos ingresados (por ejemplo, precio sea numérico).
🔹 Invocar a insert_productos() para persistir el registro en el archivo productos.csv.

Ejemplo de ejecución:
--------------------------------
Ingrese el nombre del producto: Zapatillas Urbanas
Ingrese la categoría: Calzado
Ingrese el precio unitario: 32000
✅ Producto agregado correctamente.
--------------------------------
"""

# Ejercicio 6
"""
Test Unitarios con Pytest

Crear un archivo test_productos.py y escribir pruebas unitarias para las funciones:

🔹 read_productos()
🔹 write_productos()
🔹 insert_productos()
🔹 inicializar_productos()

Recomendaciones:
✅ Utilizar un archivo temporal (por ejemplo test_productos.csv).
✅ Verificar que se escriben las líneas correctas.
✅ Verificar que insert_productos() agrega una línea al final.
✅ Asegurarse de que read_productos() maneje correctamente el caso de archivo inexistente.

Ejemplo:

def test_insert_productos():
    producto = [4, "Buzo Negro", "Indumentaria", 21000.0]
    insert_productos("test_productos.csv", producto)
    data = read_productos("test_productos.csv")
    assert any(row[1] == "Buzo Negro" for row in data)
"""