import storage


# Leer todos los estudiantes del storage
def get_all_estudiantes():
    """
    parametros: None
    return: data
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "estudiantes.json"

    # invoco a read_data para recuperar los datos del archivo
    data = storage.read_data(FILE_NAME)
    return data


# Buscar en el storage un estudiante por su id
def get_estudiante_by_id(id_estudiante):
    """
    parametros: id str
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "estudiantes.json"
    estudiantes = get_all_estudiantes()
    if len(estudiantes) == 0:
        raise Exception("get_all_students retorno 0")

    # Buscar coincidencia
    for e in estudiantes:
        if str(e["id_estudiante"]) == id_estudiante:
            return e

    # Si no se encontró
    return False


def add_estudiante(new_estudiante):
    """
    parametros: estudiante (lista)
    return: True
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "estudiantes.json"

    estudiantes = get_all_estudiantes()
    if len(estudiantes) == 0:
        new_estudiante["id_estudiante"] = 1
    else:
        last_id = estudiantes[-1]["id_estudiante"]
        next_id = last_id + 1
        new_estudiante["id_estudiante"] = next_id

    estudiantes.append(new_estudiante)
    # invoco a write_data para persistir el dato en el archivo
    storage.write_data(FILE_NAME, estudiantes)
    return True


def delete_estudiante_by_id(id_estudiante):
    """
    parametros: id_estudiante str
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "estudiantes.json"
    estudiantes = get_all_estudiantes()

    # Buscar coincidencia
    flag = False
    for e in estudiantes:
        if str(e["id_estudiante"]) == id_estudiante:
            estudiantes.remove(e)
            flag = True
            break
    if not flag:
        raise Exception("No se ha encontrado el estudiante que se desea eliminar")

    storage.write_data(FILE_NAME, estudiantes)

    return True


# Leer todos las asistencias del storage
def get_all_asistencias():
    """
    parametros: None
    return: data
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "asistencias.json"

    # invoco a read_data para recuperar los datos del archivo
    data = storage.read_data(FILE_NAME)
    return data


def registrar_asistencia(new_asistencia):
    """
    parametros: asistencia = {"id_estudiante": ?, "asignatura_nombre": ?, "asignatura_codigo": ?, "estado": ?, "fecha": ? }
    return: true
    """
    # inicializo la constante con el nombre del archivo
    FILE_NAME = "asistencias.json"
    asistencias = get_all_asistencias()
    if len(asistencias) == 0:
        new_asistencia["id_asistencia"] = 1
    else:
        last_id = asistencias[-1]["id_asistencia"]
        next_id = last_id + 1
        new_asistencia["id_asistencia"] = next_id

    asistencias.append(new_asistencia)
    storage.write_data(FILE_NAME, asistencias)
    return True