from source.osm_services import *
from source.utilities import *

# def test_get_geolocation_1():
#     direccion = {
#         "calle": "Lima",
#         "altura": "775",
#         "ciudad": "Ciudad de Buenos Aires"
#     }
#     lat, lon = get_geolocation(direccion)
#     assert lat == '-34.6170769', "Lat debe ser -34.6170769"
#     assert lon == '-58.3822460',  "Lon debe ser -58.3822460"

# def test_get_geolocation_2():
#     direccion = {
#         "calle": "Libertad",
#         "altura": "1340",
#         "ciudad": "Ciudad de Buenos Aires"
#     }
#     lat, lon = get_geolocation(direccion)
#     assert lat == '-34.5919018', "Lat debe ser -34.5919018"
#     assert lon == '-58.3844548',  "Lon debe ser -58.3844548"


import pytest

@pytest.mark.parametrize("direccion,lat_esperada,lon_esperada", [
    ({"calle": "Lima", "altura": "775", "ciudad": "Ciudad de Buenos Aires"}, '-34.6170769', '-58.3822460'),
    ({"calle": "Libertad", "altura": "1340", "ciudad": "Ciudad de Buenos Aires"}, '-34.5919018', '-58.3844548'),
])
def test_get_geolocation(direccion, lat_esperada, lon_esperada):
    lat, lon = get_geolocation(direccion)
    assert lat == lat_esperada, f"Lat debe ser {lat_esperada}"
    assert lon == lon_esperada, f"Lon debe ser {lon_esperada}"



def test_calcular_distancia():
    geo_inicial = (-34.6170769, -58.3822460)
    geo_final = (-34.5919018, -58.3844548)
    distancia = calcular_distancia(geo_inicial, geo_final)
    assert distancia == 2.8, "La distancia debe ser 2.8"