import services
import print_console
import input_handlers
import read_console
import menu_1_handlers
import menu_2_handlers
import menu_3_handlers
import sys


def handle_opcion_1():
    while True:
        print_console.print_menu_1()
        opcion = read_console.get_menu_opcion()
        match opcion:
            case "1":
                # 1. Para ver todos los estudiantes
                menu_1_handlers.handle_menu_1_opcion_1()
            case "2":
                # 2. Para buscar estudiante por legajo
                menu_1_handlers.handle_menu_1_opcion_2()
            case "3":
                # 3. Para agregar nuevo estudiante
                menu_1_handlers.handle_menu_1_opcion_3()
            case "4":
                # 4. Para editar estudiante
                menu_1_handlers.handle_menu_1_opcion_4()
            case "5":
                # 5. Para eliminar estudiante
                menu_1_handlers.handle_menu_1_opcion_5()
            case "6":
                # Volver
                break

def handle_opcion_2():
    while True:
        print_console.print_menu_2()
        opcion = read_console.get_menu_opcion()
        match opcion:
            case "1":
                # 1. Procesar asistencias
                menu_2_handlers.handle_menu_2_opcion_1()
            case "2":
                # Volver
                break

def handle_opcion_3():
    while True:
        print_console.print_menu_3()
        opcion = read_console.get_menu_opcion()
        match opcion:
            case "1":
                # Reporte 1: Estudiantes Join Asistencias
                menu_3_handlers.handle_menu_3_opcion_1()
            case "2":
                # Reporte 2: Asistencias por asignatura
                menu_3_handlers.handle_menu_3_opcion_2()
            case "3":
                # Reporte 3: Asistencias por estudiantes
                menu_3_handlers.handle_menu_3_opcion_3()
            case "4":
                # Volver
                break

