import read_console


def input_estudiante():
    """
    return: lista
    """
    nombre = read_console.input_nombre_estudiante()
    apellido = read_console.input_apellido_estudiante()
    legajo = read_console.input_legajo_estudiante()
    return {"nombre": nombre, "apellido": apellido, "legajo": legajo}


def input_id_estudiante():
    """
    return str numerico
    """
    id_estudiante = read_console.input_id_estudiante()
    return id_estudiante


def input_confirma_eliminar_estudiante():
    """
    return True/False
    """
    confirma = read_console.input_confirma_eliminar_estudiante()
    return True if confirma == "s" else False


def input_asistencia():
    id_estudiante = read_console.input_id_estudiante()
    asignatura_nombre = read_console.input_asignatura_nombre()
    asignatura_codigo = read_console.input_asignatura_codigo()
    estado = read_console.input_estado()
    fecha = read_console.input_fecha()
    return {
        "id_estudiante": id_estudiante,
        "asignatura_nombre": asignatura_nombre,
        "asignatura_codigo": asignatura_codigo,
        "estado": estado,
        "fecha": fecha
    }