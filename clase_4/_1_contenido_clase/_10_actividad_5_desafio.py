# Dados 

import random
from functools import reduce

# Lista de datos (matriz de alumnos)
estudiantes = [
    [1, "Thiago", "Almada", 19],
    [2, "Agostina", "Hein", 25],
    [3, "Leandro", "Bolmaro", 22],
    [4, "Valentina", "Raposo", 24],
]

# Lista de datos (matriz de cursos)
cursos = [
    [34069, "Fundamentos de Informatica", "Monserrat", "miercoles", "18:30"],
    [34071, "Programacion I", "Monserrat", "jueves", "18:30"],
    [31051, "Algebra", "Monserrat", "lunes", "18:30"],
]

# Lista de datos (matriz de registros de asistencia)
est_cursos = [
    [34069, 1],
    [34069, 2],
    [34069, 3],
    [34069, 4],
    [34071, 1],
    [34071, 2],
    [34071, 3],
    [34071, 4],
    [31051, 1],
    [31051, 2],
    [31051, 3],
    [31051, 4],
]

def simular_asistencias(asistencias, n_clases):
    for asistencia in asistencias:
        asistencia.append([True if random.randint(0,1) == 1 else False for _ in range(n_clases)])

def computar_asistencias(est_cursos, cursos, estudiantes):
    computo_asistencias = [] 
    for item in est_cursos:
        computo1 = []
        computo1.extend(item[:2])
        computo1.append(reduce(lambda a, b: a+b , item[-1]))
        computo_asistencias.append(computo1)
    return computo_asistencias

simular_asistencias(est_cursos, 16)
asistencias = computar_asistencias(est_cursos, cursos, estudiantes)


print(asistencias)

