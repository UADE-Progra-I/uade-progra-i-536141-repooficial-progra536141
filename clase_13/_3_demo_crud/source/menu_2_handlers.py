import services
import print_console
import input_handlers
import read_console
import sys



# 1. Procesar asistencias
def handle_menu_2_opcion_1():
    try:
        # Listamos los usuarios
        estudiantes = services.get_all_estudiantes()
        print_console.print_estudiantes(estudiantes)
        # Usuario ingresa los datos de la asistencia a registrar
        asistencia = input_handlers.input_asistencia()
        services.registrar_asistencia(asistencia)
        return True
    except Exception as e:
        print_console.print_error(e)
        return


