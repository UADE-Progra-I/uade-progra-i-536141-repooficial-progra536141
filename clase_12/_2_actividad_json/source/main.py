# import librerias
import input_handlers
import osm_services
import utilities


# Declaracion de funciones
def main():
    while True:
        print("\nIngrese la dirección inicial: ")
        direccion_inicial = input_handlers.get_direccion()
        print("\nIngrese la dirección final: ")
        direccion_final = input_handlers.get_direccion()

        try:
            # Obtener las coordenadas de la direccion_incial
            geo_inicial = osm_services.get_geolocation(direccion_inicial)
            # Obtener las coordenadas de la direccion_final
            geo_final = osm_services.get_geolocation(direccion_final)

            # Convertir la tupla de coordenadas de str a float
            geo_inicial = (float(x) for x in geo_inicial)
            # Convertir la tupla de coordenadas de str a float
            geo_final = (float(x) for x in geo_final)

            # Invocar a la función que calcula la distancia
            distancia = utilities.calcular_distancia(geo_final, geo_inicial)
            print(f"\nLa distancia calculada es de: {distancia} kilómetros")
        except Exception as e:
            print(f"ERROR: {e}")

        continua = input("\nContinúa? s/n: ")
        if continua.strip().lower() == "n":
            break

if __name__ == "__main__":
    main()
