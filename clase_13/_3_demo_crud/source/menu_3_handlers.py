import services
import print_console
import input_handlers
import read_console
import sys


# 1. Reporte 1: Estudiantes Join Asistencias
def handle_menu_3_opcion_1():
    # Importar librerías
    import pandas as pd

    # Cargar datos de archivos
    estudiantes = services.get_all_estudiantes()
    asistencias = services.get_all_asistencias()

    # Convertir tipo diccionario a DataFrame
    df_e = pd.DataFrame(estudiantes)
    df_a = pd.DataFrame(asistencias)

    # Convertir tipo de dato a str antes de hacer el join
    df_e["id_estudiante"] = df_e["id_estudiante"].astype(str)
    df_a["id_estudiante"] = df_a["id_estudiante"].astype(str)

    # Hacer el join entre DataFrames
    df_ea = pd.merge(df_e, df_a, how="inner", on="id_estudiante").sort_values(by="id_asistencia")
    print(df_ea)

# 2. Reporte 2: Asistencias por asignaturas






def handle_menu_3_opcion_2():
    # Importar librerías
    import pandas as pd

    # Cargar datos de archivos
    asistencias = services.get_all_asistencias()

    # Convertir tipo diccionario a DataFrame
    df_a = pd.DataFrame(asistencias)

    df_agg = (
        df_a.groupby(["asignatura_nombre", "asignatura_codigo", "estado"])
        .size()
        .unstack(fill_value=0)
        .reset_index()
    )

    print(df_agg)

    # df_agg1 = df_agg.query("asignatura_nombre == 'Progra I'")
    # print(df_agg1)