def print_menu():
    print(
"""
Elegir una opción:
1. Para ver todos los estudiantes
2. Para buscar estudiante por legajo
3. Para agregar nuevo estudiante
4. Para editar estudiante
5. Para eliminar estudiante
6. Procesar asistencias
7. Generar reporte de asistencias
8. Para salir
"""
    )


def print_estudiante(e):
    print(f"Id: {e['id_estudiante']} - Nombre: {e['nombre']} - Apellido: {e['apellido']} - Legajo: {e['legajo']}")

def print_estudiantes(estudiantes):
    for e in estudiantes:
        print(f"Id: {e['id_estudiante']} - Nombre: {e['nombre']} - Apellido: {e['apellido']} - Legajo: {e['legajo']}")

def print_asistencias(asistencias):
    for asistencia in asistencias:
        for key, value in asistencia.items():
            print(f"{key}: {value}")
        

def print_success(message):
    print(message)

def print_warning(warning):
    print(f"ATENCION: {warning}")

def print_error(error):
    print(f"ERROR: {error}")

