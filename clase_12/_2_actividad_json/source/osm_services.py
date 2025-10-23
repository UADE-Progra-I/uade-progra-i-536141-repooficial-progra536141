def get_geolocation(direccion):
    # TO DO validar argumentos

    import requests
    calle = direccion.get('calle')
    altura = str(direccion.get('altura'))
    ciudad = direccion.get('ciudad')
    ciudad_split = ciudad.split()
    url = f"https://nominatim.openstreetmap.org/search?q={calle + " " + altura + " " + ciudad}&format=json"

    # Es buena práctica incluir un user-agent identificativo
    headers = {"User-Agent": "MiAplicacionPython/1.0"}

    respuesta = requests.get(url, headers=headers)
    data = respuesta.json()

    # Iteramos la lista de diccionarios y buscamos el mejor match
    coincidencia = False
    for item in data:
        if all(palabra.lower() in item["display_name"].lower() for palabra in ciudad_split):
            return item["lat"], item["lon"]
    if not coincidencia:
        raise Exception(f"no se encontraron coordenadas para la dirección {calle} {altura}, {ciudad}")
