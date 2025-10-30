def print_menu():
    print(
"""
Elegir una opción:
1. Gestionar Estudiantes
2. Gestionar Asistencias
3. Generar Reportes
4. Salir
"""
    )

# Menu 1: Gestionar Estudiantes
def print_menu_1():
    print("""
1. Para ver todos los estudiantes
2. Para buscar estudiante por legajo
3. Para agregar nuevo estudiante
4. Para editar estudiante
5. Para eliminar estudiante
6. Volver
""")
    
# Menu 2: Gestionar Asistencias
def print_menu_2():
    print("""
1. Procesar asistencias
2. Volver
""")

# Menu 3: Generar Reportes
def print_menu_3():
    print("""
1. Reporte 1: Estudiantes Join Asistencias
2. Reporte 2: Asistencias por asignaturas
3. Reporte 3: Asistencias por estudiantes
4. Volver
""")



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

