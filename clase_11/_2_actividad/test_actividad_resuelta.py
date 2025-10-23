import os
import csv
import pytest
from actividad_resuelta import (
    write_productos,
    read_productos,
    insert_productos,
    inicializar_productos,
    FILE_PATH,
)

def test_write_and_read_productos():
    data = [[1, "Remera Azul", "Indumentaria", 9500.50]]
    write_productos(data)
    result = read_productos()
    assert len(result) == 1
    assert result[0][1] == "Remera Azul"


def test_insert_productos():
    producto = [2, "Campera Negra", "Indumentaria", 20000.00]
    insert_productos(producto)
    result = read_productos()
    assert any(row[1] == "Campera Negra" for row in result)


def test_inicializar_productos():
    inicializar_productos()
    result = read_productos()
    assert len(result) == 3 # 3 productos
