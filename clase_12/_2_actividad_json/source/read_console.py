

def input_calle():
        while True:
            try:
                calle = input("Ingrese la calle: ")
                if not calle:
                     raise ValueError("La calle no puede estar en blanco")
                return calle
            except Exception as e:
                 print(f"ERROR: {e}")

def input_altura():
        while True:
            try:
                altura = int(input("Ingrese la altura: "))
                return altura
            except ValueError:
                 print(f"ERROR: altura incorrecta, intente nuevamente...")
            except Exception as e:
                 print(f"ERROR: {e}")

def input_ciudad():
        while True:
            try:
                ciudad = input("Ingrese la ciudad: ")
                if not ciudad:
                     raise ValueError("La calle no puede estar en blanco")
                return ciudad
            except Exception as e:
                 print(f"ERROR: {e}")
