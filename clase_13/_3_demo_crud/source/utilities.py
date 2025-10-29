import re



def validar_menu_opcion(opcion):
    if opcion == "":
        raise ValueError("Opción en blanco")
    # Patrón que acepta solo los números del 1 al 6
    patron = r"^[1-8]$"
    if not re.match(patron, opcion):
        raise ValueError("Debe ingresar un número entre 1 y 8")
    return True

def validar_asistencia_estado(estado):
    if estado == "":
        raise ValueError("Estado en blanco")
    # Patrón que acepta solo AaPpMm
    patron = r"^[AaPpMm]$"
    if not re.match(patron, estado):
        raise ValueError("Debe ingresar P - presente, A - ausente - M: media falta")
    return True

def validar_asistencia_fecha(fecha):
    if fecha == "":
        raise ValueError("Estado en blanco")
    # Patrón que acepta formato dd/mm/aaaa
    patron = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$"
    if not re.match(patron, fecha):
        raise ValueError("Debe ingresar dd/mm/aaaa")
    return True

