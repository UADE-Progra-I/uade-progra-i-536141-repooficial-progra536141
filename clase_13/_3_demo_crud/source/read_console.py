import utilities

def get_menu_opcion():
    while True:
        try:
            opcion = input("Ingrese su opción: ").strip()
            utilities.validar_menu_opcion(opcion)
            return opcion
        except Exception as e:
            print(f"ERROR: {e}")
        
def input_nombre_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    # TO DO: agregar validación al nombre
    return nombre

def input_apellido_estudiante():
    apellido = input("Ingrese el apellido del estudiante: ")
    # TO DO: agregar validación al apellido
    return apellido

def input_legajo_estudiante():
    legajo = input("Ingrese el legajo del estudiante: ")
    # TO DO: agregar validación a la edad
    return legajo

def input_id_estudiante():
    id_estudiante = input("Ingrese el id del estudiante: ")
    # TO DO: agregar validación al ID
    return id_estudiante

def input_confirma_eliminar_estudiante():
    confirma = input("Confirma que desea eliminar el estudiante: s/n?")
    return confirma.strip().lower()

def input_asignatura_nombre():
    asignatura_nombre = input("Ingrese el nombre de la asignatura: ")
    # TO DO: agregar validación
    return asignatura_nombre

def input_asignatura_codigo():
    input_asignatura_codigo = input ("Ingrese el código de la asignatura: ")
    # TO DO: agregar validación
    return input_asignatura_codigo

def input_estado():
    while True:
        try:
            estado = input ("Ingrese el estado (P - presente, A - ausente - M: media falta): ")
            utilities.validar_asistencia_estado(estado)
            return estado
        except Exception as e:
            print(f"ERROR: {e}")

def input_fecha():
    while True:
        try:
            fecha = input ("Ingrese la fecha en formato dd/mm/aaaa: ")
            utilities.validar_asistencia_fecha(fecha)
            return fecha
        except Exception as e:
            print(f"ERROR: {e}")


    
 

