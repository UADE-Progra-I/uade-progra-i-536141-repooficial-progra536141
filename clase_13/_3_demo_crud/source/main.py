import print_console
import read_console
import menu_handlers

def main():

    while True:
        print_console.print_menu()
        opcion = read_console.get_menu_opcion()
        match opcion:
            case "1":
                # 1. Gestionar Estudiantes
                menu_handlers.handle_opcion_1()
            case "2":
                # 2. Gestionar Asistencias
                menu_handlers.handle_opcion_2()
            case "3":
                # 3. Generar Reportes
                menu_handlers.handle_opcion_3()
            case "4":
                break

    print(f"Gracias por usar nuestra APP")



if __name__ == "__main__":
    main()