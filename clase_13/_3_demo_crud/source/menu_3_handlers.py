import services
import print_console
import input_handlers
import read_console
import sys


# Reporte 1: Estudiantes Join Asistencias
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
    df_ea = pd.merge(df_e, df_a, on="id_estudiante", how="left",).sort_values(by="id_asistencia")
    print(df_ea)


# Reporte 2: Asistencias por asignaturas
def handle_menu_3_opcion_2():
    # Importar librerías
    import pandas as pd

    # Cargar datos de archivos
    asistencias = services.get_all_asistencias()

    # Convertir tipo diccionario a DataFrame
    df_a = pd.DataFrame(asistencias)

    # df_agg = (
    #     df_a.groupby(["asignatura_nombre", "asignatura_codigo", "estado"])
    #     .size()
    #     .unstack(fill_value=0)
    #     .reset_index()
    # )

    df_fil = df_a.copy()
    df_fil["estado_p"] = df_fil[df_fil['estado'].str.contains('p', case=False)]["estado"]
    df_fil["estado_a"] = df_fil[df_fil['estado'].str.contains('a', case=False)]["estado"]
    df_fil["estado_m"] = df_fil[df_fil['estado'].str.contains('m', case=False)]["estado"]
    df_agg = df_fil.groupby(["asignatura_nombre", "asignatura_codigo"]).agg(
        Presentes = ('estado_p', 'count'),
        Ausentes = ('estado_a', 'count'),
        Media_falta = ('estado_m', 'count'),
    )
    print(df_agg)

# Reporte 3: Asistencias por estudiantes
def handle_menu_3_opcion_3():
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

    # Filtramos los presentes
    df_fil = df_ea[df_ea['estado'].str.contains('p', case=False)]
    df_agg = df_fil.groupby(["nombre", "apellido"]).agg(
        Asistencias = ('estado', 'count')
    )
       
    print(df_agg)