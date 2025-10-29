import services
import print_console
import input_handlers
import sys

def handle_opcion_1():
    try:
        estudiantes = services.get_all_estudiantes()
        print_console.print_estudiantes(estudiantes)
    except FileNotFoundError:
        print_console.print_warning("Debe primero crear un registro")
    except Exception as e:
        print_console.print_error(e)

def handle_opcion_3():
    try:
        estudiante = input_handlers.input_estudiante()
        services.add_estudiante(estudiante)
        print_console.print_success("Estudiante agregado exitosamente")
    except Exception as e:
        print_console.print_error(e)

def handle_opcion_5():
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

# Opción 6: registrar asistencia
def handle_opcion_6():
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

# Opción 7: Generar reporte de asistencias
def handle_opcion_7():
    estudiantes = services.get_all_estudiantes()
    asistencias = services.get_all_asistencias()
    import pandas as pd
    df_e = pd.DataFrame(estudiantes)
    df_a = pd.DataFrame(asistencias)
    df_e["id_estudiante"] = df_e["id_estudiante"].astype(str)
    df_a["id_estudiante"] = df_a["id_estudiante"].astype(str)
    df_ea = pd.merge(df_e, df_a, how="left", on="id_estudiante").sort_values(by="id_asistencia")
    df_agg = (
        df_ea.groupby(["asignatura_nombre", "asignatura_codigo", "estado"])
        .size()
        .unstack(fill_value=0)
        .reset_index()
    )

    df_agg1 = df_agg.query("asignatura_nombre == 'Progra I'")
    print(df_agg1)

