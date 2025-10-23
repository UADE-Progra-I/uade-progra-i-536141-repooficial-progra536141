from source.storage import *


def test_write_read_estudiantes():
    FILE_NAME = "test_estudiantes.json"
    data = [{"id": 1, "nombre": "John", "apellido": "Doe", "edad": 23}]
    write_data(FILE_NAME, data)
    response = read_data(FILE_NAME)
    assert len(response) == 1, "Debe retornar solo 1 registro"
    assert response[0]["nombre"] == "John", "El nombre debe ser John"


