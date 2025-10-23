import read_console

def get_direccion():
    return {
        "calle": read_console.input_calle(),
        "altura": read_console.input_altura(),
        "ciudad": read_console.input_ciudad()
    }