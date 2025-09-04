import re

cadena = "Peter Piper picked a peck of pickled peppers"

# Metodo search()

match = re.search("pi", cadena.lower())
print("Objeto result:", match)
print("Coincidencia:", match.group())
print("Posición inicial:", match.start())
print("Posición final:", match.end())
print("Rango de índices:", match.span())
print(cadena)

# Metodo findall
# Case 1
match1 = re.findall("pi", cadena)
print("\n" + cadena)
print('re.findall("pi", cadena): ', match1)

match2 = re.findall("pi", cadena, re.IGNORECASE)
print("\n" + cadena)
print('re.findall("pi", cadena, re.IGNORECASE)', match2)


# Metacaracteres
# El . es un comodin
match3 = re.findall("p.c", cadena)
print("\n" + cadena)
print('re.findall("p.c", cadena)', match3)

# Con ^ el pattern se busca solo al inicio
match4 = re.findall("^pi", cadena)
print("\n" + cadena)
print('re.findall("^pi", cadena)', match4)

# Con ^ el pattern se busca solo al inicio, agregamos split()
cadena_split = cadena.split()  # genera una lista de str
match5 = [word for word in cadena_split if re.findall("^pi", word)]
print("\n", cadena_split)
print('re.findall("^pi", word)', match5)

# Con $ el pattern se busca solo al final
match6 = [word for word in cadena_split if re.findall("ed$", word)]
print("\n", cadena_split)
print('re.findall("ed$", word)', match5)

# Combinamos ^ con $
match6 = [word for word in cadena_split if re.findall("^pi.*ed$", word)]
print("\n", cadena_split)
print('re.findall("^pi.*ed$", word)', match6)


# Escape de caracteres \$
cadena_especial = "Las acciones de Apple cerraron a $238.47 usd"
match7 = [word for word in cadena_especial.split() if re.findall(r"^\$", word)]
print("\n", cadena_especial)
print('re.findall(r"\$", word)', match7)


# Escape de caracteres \.
cadena_especial = "Las acciones de Apple cerraron a $238.47 usd"
match8 = re.findall(r"\.", cadena_especial)
match9 = [word for word in cadena_especial.split() if re.findall(r"\.", word)]
print("\n" + cadena_especial)
print('re.findall(r"\.", cadena_especial)]', match8)
print('re.findall(r"\.", word)', match9)

# Grupo de caracteres []
text = "En un rato llega el pato a la granja de Tato"
match10 = re.findall("[pr]ato", text)
print("\n" + text)
print('re.findall("[pr]ato", text)', match10)

# Rango de caracteres [a-z], [0-9]
direccion = "Lima 757 Piso 5"
match11 = re.findall("[a-z]", direccion)
match12 = re.findall("[0-9]", direccion)
print("\n" + direccion)
print('re.findall("[a-z]", direccion)', match11)
print('re.findall("[0-9]", direccion)', match12)

# Rango de caracteres [a-z] con ^ para negar un conjunto
match13 = re.findall("[^0-9]", direccion, re.IGNORECASE)
print("\n" + direccion)
print('re.findall("[^0-9]", direccion)', match13)

text = "La bella y enorme casa se veía desde el tren."
match14 = [word for word in text.split() if re.findall("^[b-g]", word)]
match15 = [word for word in text.split() if re.findall("[b-g]$", word)]
print("\n" + text)
print('re.findall("^[b-g]", word)', match14)
print('re.findall("[b-g]$", word)', match15)


# Cuantificadores o multiplicadores
numeros = ["12", "102", "1002", "10002"]
match16 = [numero for numero in numeros if re.findall("10?2", numero)]
match17 = [numero for numero in numeros if re.findall("10*2", numero)]
match18 = [numero for numero in numeros if re.findall("10+2", numero)]
print("\n" + str(numeros))
print('re.findall("1?2", numero): ', match16)
print('re.findall("1*2", numero): ', match17)
print('re.findall("1+2", numero): ', match18)

# Delimitacion
text = "Juan tiene el télefono 1234-5678, Oliver tiene el teléfono 11-15-3456-7890 y Gabriela el 11-15-7654-3210."
patron = "([0-9]{2,})-(15-[0-9]{4})-([0-9]{4})"
numeros = re.findall(patron, text)
print("\n" + str(numeros))  # [('11', '15-3456', '7890'), ('11', '15-7654', '3210')]
# Imprimimos los números de celulares encontrados y sus partes específicas
if numeros:
    print("Números de celulares encontrados:")
    for numero in numeros:
        print(f"Número completo: {numero[0]}-{numero[1]}-{numero[2]}")
        print(f"Código de área: {numero[0]}\n")
else:
    print("No se encontraron números de teléfono.")

# Modo sub
# Reemplazar todas las ocurrencias de 'elefantes' por 'dinosaurios'
text = "Los elefantes se extinguieron hace millones de años. Se han encontrado restos de elefantes enterrados."
match19 = re.sub("elefantes", "dinosaurios", text)
print(match19)


text = "El número de teléfono de Oliver es 123-456-7890, y el de Gabriela es 987-654-3210."
patron = "[0-9]{3}-[0-9]{3}-[0-9]{4}"
cadenaEnmascarada = "XXX-XXX-XXXX"
# Utilizamos re.sub() para reemplazar todos los números de teléfono por la cadena enmascarada
textOfuscado = re.sub(patron, cadenaEnmascarada, text)
print("\nTexto original:")
print(text)
print("\nTexto después de ofuscar los números de teléfono:")
print(
    textOfuscado
)  # El número de teléfono de Oliver es XXX-XXX-XXXX, y el de Gabriela es XXX-XXX-XXXX.

# re.split
text = "Hola, ¿cómo estás? Espero que bien. Yo estoy bien también."
text_split = text.split()
text_re_split = re.split(r"[., ]", text)
print("\n" + text)
print("text.split(): ", text_split)
print("re.split('[.,]', text): ", text_re_split)


# match
cadenas = ["A123", "B456", "C789", "123A", "D1234"]
patron = "[A-Za-z][1-3]{3}"
match20 = [
    (
        f'{cadena} coincide con el patrón.'
        if re.match(patron, cadena)
        else f'{cadena} no coincide con el patrón.'
    )
    for cadena in cadenas
]
print("\n", cadenas)
for item in match20:
    print(item)

# compile
patron = re.compile('[0-9]{4}')
cadena = "07/08/2017|03/02/1984|17/03/1984"
coincidencias = patron.findall(cadena)
print(f'\nCoincidencias encontradas con findall(): {coincidencias}') # Coincidencias encontradas con findall(): ['2017', '1984', '1984']

inicioCoincidencia = patron.match(cadena)
print(f'Coincidencia al inicio con match(): {inicioCoincidencia}') # Coincidencia al inicio con match(): None

cadenaReemplazada = patron.sub('XXXX', cadena)
print(f'Cadena después de usar sub(): {cadenaReemplazada}') # Cadena después de usar sub(): 07/08/XXXX|03/02/XXXX|17/03/XXXX

