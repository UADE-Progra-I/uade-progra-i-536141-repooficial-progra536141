-- Crear el esquema (opcional, podés omitirlo si querés usar "public")
CREATE SCHEMA IF NOT EXISTS universidad;
SET search_path TO universidad;

-- Tabla de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    legajo VARCHAR(20) UNIQUE NOT NULL
);

-- Tabla de asistencias
CREATE TABLE IF NOT EXISTS asistencias (
    id_asistencia SERIAL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    asignatura_nombre VARCHAR(100) NOT NULL,
    asignatura_codigo VARCHAR(20) NOT NULL,
    estado VARCHAR(20),
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


-- insertar estudiantes
INSERT INTO estudiantes (id_estudiante, nombre, apellido, legajo) VALUES
(1, 'John', 'Doe', 13254),
(2, 'Chris', 'Hartman', 125584),
(3, 'Viktor', 'Halley', 32114);

-- insertar registro de asistencias
INSERT INTO asistencias (
    id_asistencia,
    id_estudiante,
    asignatura_nombre,
    asignatura_codigo,
    estado,
    fecha
) VALUES
(1, 1, 'Álgebra I', '2799', 'A', '2025-10-22'),
(2, 2, 'Progra I', '5421', 'M', '2025-10-24'),
(3, 1, 'Progra I', '5421', 'M', '2025-10-18'),
(4, 1, 'Álgebra I', '2799', 'M', '2025-10-23'),
(5, 3, 'Estadística', '3589', 'A', '2025-10-04'),
(6, 3, 'Álgebra I', '2799', 'M', '2025-10-10'),
(7, 2, 'Álgebra I', '2799', 'P', '2025-10-21'),
(8, 3, 'Progra I', '5421', 'P', '2025-10-15'),
(9, 2, 'Estadística', '3589', 'A', '2025-10-11'),
(10, 3, 'Estadística', '3589', 'M', '2025-10-23'),
(11, 2, 'Progra I', '5421', 'M', '2025-10-18'),
(12, 3, 'Álgebra I', '2799', 'A', '2025-10-17'),
(13, 2, 'Estadística', '3589', 'A', '2025-10-09'),
(14, 2, 'Progra I', '5421', 'A', '2025-10-17'),
(15, 2, 'Progra I', '5421', 'P', '2025-10-05'),
(16, 3, 'Estadística', '3589', 'P', '2025-10-10'),
(17, 2, 'Álgebra I', '2799', 'P', '2025-10-16'),
(18, 3, 'Estadística', '3589', 'M', '2025-10-18'),
(19, 2, 'Álgebra I', '2799', 'A', '2025-10-02'),
(20, 3, 'Estadística', '3589', 'A', '2025-10-08'),
(21, 1, 'Estadística', '3589', 'A', '2025-10-20'),
(22, 3, 'Álgebra I', '2799', 'M', '2025-10-04'),
(23, 2, 'Álgebra I', '2799', 'M', '2025-10-06'),
(24, 1, 'Estadística', '3589', 'P', '2025-10-09'),
(25, 3, 'Progra I', '5421', 'A', '2025-10-05'),
(26, 2, 'Estadística', '3589', 'P', '2025-10-03'),
(27, 2, 'Progra I', '5421', 'P', '2025-10-25'),
(28, 2, 'Álgebra I', '2799', 'A', '2025-10-17'),
(29, 1, 'Progra I', '5421', 'A', '2025-10-16'),
(30, 2, 'Álgebra I', '2799', 'M', '2025-10-06'),
(31, 1, 'Estadística', '3589', 'M', '2025-10-13'),
(32, 2, 'Progra I', '5421', 'P', '2025-10-14'),
(33, 1, 'Estadística', '3589', 'P', '2025-10-20'),
(34, 3, 'Estadística', '3589', 'M', '2025-10-05'),
(35, 1, 'Progra I', '5421', 'M', '2025-10-23'),
(36, 2, 'Progra I', '5421', 'P', '2025-10-07'),
(37, 3, 'Estadística', '3589', 'M', '2025-10-12'),
(38, 1, 'Progra I', '5421', 'P', '2025-10-09'),
(39, 2, 'Álgebra I', '2799', 'P', '2025-10-09'),
(40, 2, 'Álgebra I', '2799', 'A', '2025-10-13'),
(41, 3, 'Estadística', '3589', 'A', '2025-10-01'),
(42, 3, 'Progra I', '5421', 'A', '2025-10-14'),
(43, 1, 'Estadística', '3589', 'A', '2025-10-15'),
(44, 3, 'Álgebra I', '2799', 'P', '2025-10-21'),
(45, 1, 'Progra I', '5421', 'M', '2025-10-18'),
(46, 3, 'Progra I', '5421', 'P', '2025-10-20'),
(47, 1, 'Progra I', '5421', 'P', '2025-10-17'),
(48, 2, 'Progra I', '5421', 'M', '2025-10-19'),
(49, 2, 'Progra I', '5421', 'M', '2025-10-10'),
(50, 3, 'Estadística', '3589', 'M', '2025-10-11');


-- Seleccionar todos los campos de estudiantes
select * from estudiantes;


-- Seleccionar todos los campos de asistencias
select * from asistencias;


-- Seleccionar campos especificos
select id_estudiante, apellido, legajo
from estudiantes;


-- Seleccionar todos los estudiantes que tienen asistencias
select * 
from estudiantes e
join asistencias a on e.id_estudiante = a.id_estudiante


-- Calcular el presentismos de cada asignatura
select asignatura_nombre, asignatura_codigo, count(estado) as presentismo
from asistencias
where estado like '%P%'
group by asignatura_nombre, asignatura_codigo


-- Calcular el presentismos de cada estudiante
select nombre, apellido, legajo, count(estado) as presentismo
from estudiantes e
join asistencias a on e.id_estudiante = a.id_estudiante
where estado like '%P%'
group by nombre, apellido, legajo


-- Calcular el presentismos de cada estudiante por asignatura
select asignatura_nombre, nombre, apellido, legajo, count(estado) as presentismo
from estudiantes e
join asistencias a on e.id_estudiante = a.id_estudiante
where estado like '%P%'
group by asignatura_nombre, nombre, apellido, legajo
order by asignatura_nombre, legajo


-- Calcular el asistencias de cada estudiante
SELECT 
    e.nombre, 
    e.apellido, 
    e.legajo,
    SUM(CASE WHEN a.estado LIKE '%P%' THEN 1 ELSE 0 END) AS presentes,
    SUM(CASE WHEN a.estado LIKE '%A%' THEN 1 ELSE 0 END) AS ausentes,
    SUM(CASE WHEN a.estado LIKE '%M%' THEN 1 ELSE 0 END) AS media_falta
FROM estudiantes e
JOIN asistencias a 
    ON e.id_estudiante = a.id_estudiante
GROUP BY e.nombre, e.apellido, e.legajo;