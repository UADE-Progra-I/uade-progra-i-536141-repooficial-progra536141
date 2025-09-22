"""Dada la lista de temperaturas en °C, obtené una nueva lista
con las temperaturas en °F, redondeadas a 1 decimal.

Clue: fórmula → F = C * 9/5 + 32 y usá round(valor, 1).
"""
def conversortemp(gradosc):
    x = gradosc * 9/5 + 32
    return x 

grados = [15, 25, 10, 30, 22]
resultado = list(map(conversortemp, grados))
print(resultado) 