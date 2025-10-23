def print_menu():
    print(
"""
Elegir una opción:
1. Para ver todos los estudiantes
2. Para buscar estudiante por legajo
3. Para agregar nuevo estudiante
4. Para editar estudiante
5. Para eliminar estudiante
6. Para salir
"""
    )


def print_estudiante(e):
    print(f"Id: {e['id']} - Nombre: {e['nombre']} - Apellido: {e['apellido']} - Edad: {e['edad']}")

def print_estudiantes(estudiantes):
    for e in estudiantes:
        print(f"Id: {e['id']} - Nombre: {e['nombre']} - Apellido: {e['apellido']} - Edad: {e['edad']}")

def print_success(message):
    print(message)

def print_warning(warning):
    print(f"ATENCION: {warning}")

def print_error(error):
    print(f"ERROR: {error}")

