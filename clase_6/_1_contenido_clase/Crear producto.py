from utils.validar_producto import (
    pedir_input,
    validar_id,
    validar_nombre,
    validar_peso,
    validar_equivalencia,
    validar_categoria,
    validar_id_provedor,
    validar_stock,
    validar_producto
)

def create_product():
    id = pedir_input("Ingrese el ID del producto: ", "ID", validar_id)
    if id is None: return "No se creó el producto por datos inválidos."
    nombre = pedir_input("Ingrese el nombre del producto: ", "nombre", validar_nombre)
    if nombre is None: return "No se creó el producto por datos inválidos."
    peso = pedir_input("Ingrese el peso del producto: ", "peso", validar_peso)
    if peso is None: return "No se creó el producto por datos inválidos."
    equivalencia_venta = pedir_input("Ingrese la equivalencia de venta: ", "equivalencia_venta", validar_equivalencia)
    if equivalencia_venta is None: return "No se creó el producto por datos inválidos."
    categoria = pedir_input("Ingrese la categoría: ", "categoría", validar_categoria)
    if categoria is None: return "No se creó el producto por datos inválidos."
    id_provedor = pedir_input("Ingrese el ID del proveedor: ", "ID del proveedor", validar_id_provedor)
    if id_provedor is None: return "No se creó el producto por datos inválidos."
    stock = pedir_input("Ingrese el stock: ", "stock", validar_stock)
    if stock is None: return "No se creó el producto por datos inválidos."

    # Validación final con la función general
    es_valido, mensaje = validar_producto(id, nombre, peso, equivalencia_venta, categoria, id_provedor, stock)
    if not es_valido:
        print(f"Error: {mensaje}")
        return "No se creó el producto por datos inválidos."

    import csv
    with open('DB_CSV/produtos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nombre, peso, equivalencia_venta, categoria, id_provedor, stock])
    print("El producto se ha creado exitosamente")
    return "El producto se ha creado exitosamente"


create_product()

