# Leer y retornar el contenido de un archivo csv
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_data(file_name):
    """
    parametros:
    file_name: nombre del archivo
    """
    if not isinstance(file_name, str):
        raise TypeError("file_name debe ser un string")
    if file_name.strip() == "":
        raise ValueError("file_name no puede estar vacío")

    DATA_PATH = os.path.join(BASE_DIR, "data", file_name)

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        content = file.read().strip()
        data = json.loads(content) if content else []
    return data


def write_data(file_name, data):
    """
    parametros:
    file_name: str
    data: lista
    """
    DATA_PATH = os.path.join(BASE_DIR, "data", file_name)

    if not isinstance(file_name, str):
        raise TypeError("file_name debe ser un str")
    if file_name.strip() == "":
        raise ValueError("file_name no puede estar vacío")
    if not isinstance(data, list):
        raise TypeError("data debe ser una lista")


    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=3, ensure_ascii=True)

    return True


