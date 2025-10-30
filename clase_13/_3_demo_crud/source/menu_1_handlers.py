import services
import print_console
import input_handlers
import read_console
import sys


# 1. Para ver todos los estudiantes
def handle_menu_1_opcion_1():
    try:
        estudiantes = services.get_all_estudiantes()
        print_console.print_estudiantes(estudiantes)
    except FileNotFoundError:
        print_console.print_warning("Debe primero crear un registro")
    except Exception as e:
        print_console.print_error(e)


# 2. Para buscar estudiante por legajo
def handle_menu_1_opcion_2():
    print("Buscar estudiante por legajo *** En desarrollo ***")


# 3. Para agregar nuevo estudiante
def handle_menu_1_opcion_3():
    try:
        estudiante = input_handlers.input_estudiante()
        services.add_estudiante(estudiante)
        print_console.print_success("Estudiante agregado exitosamente")
    except Exception as e:
        print_console.print_error(e)

 # 4. Para editar estudiante
def handle_menu_1_opcion_4():
    print("Editar estudiante *** En desarrollo ***")


 # 5. Para eliminar estudiante
def handle_menu_1_opcion_5():
    try:
        # Listamos los usuarios
        estudiantes = services.get_all_estudiantes()
        print_console.print_estudiantes(estudiantes)
        # Usuario ingresa el id a eliminar
        id_estudiante = input_handlers.input_id_estudiante()
        # Buscamos el estudiante en el storage
        estudiante = services.get_estudiante_by_id(id_estudiante)
        if not estudiante:
            raise ValueError("No se ha encontrado coincidencia para ese ID")
        else:
            print_console.print_estudiante(estudiante)
            confirma_eliminar_estudiante = input_handlers.input_confirma_eliminar_estudiante()
            if confirma_eliminar_estudiante:
                services.delete_estudiante_by_id(id_estudiante)
                print_console.print_success("Estudiante eliminado exitosamente")
    except Exception as e:
        print_console.print_error(e)


