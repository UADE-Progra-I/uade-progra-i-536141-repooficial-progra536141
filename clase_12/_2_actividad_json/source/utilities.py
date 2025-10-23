def calcular_distancia(geo_inicial, geo_final):

    from geopy.distance import distance
    dist = distance(geo_final, geo_inicial).km
    return round(dist, 2)