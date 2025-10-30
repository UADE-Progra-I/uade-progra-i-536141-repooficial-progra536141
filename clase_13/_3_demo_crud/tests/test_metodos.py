from source.storage import *


def test_write_read_estudiantes():
    FILE_NAME = "test_estudiantes.json"
    data = [{"id": 1, "nombre": "John", "apellido": "Doe", "edad": 23}]
    write_data(FILE_NAME, data)
    response = read_data(FILE_NAME)
    assert len(response) == 1, "Debe retornar solo 1 registro"
    assert response[0]["nombre"] == "John", "El nombre debe ser John"


def test_registrar_asistencias():
    FILE_NAME = "test_asistencias.json"
    data = [{
        "id_asistencia": 1, 
        "id_estudiante": 1, 
        "asignatura_nombre": "Progra I", 
        "asignatura_codigo": 5421,
        "estado": "P",
        "fecha": "25/10/2025"
        }]
    write_data(FILE_NAME, data)
    response = read_data(FILE_NAME)
    assert len(response) == 1, "Debe retornar solo 1 registro"
    assert response[0]["asignatura_nombre"] == "Progra I", "El nombre debe ser Progra I"