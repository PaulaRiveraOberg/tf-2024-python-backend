-- Crear tabla persona
CREATE TABLE persona (
    persona_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    creacion TIMESTAMP DEFAULT NOW()
);

-- Crear tabla direccion
CREATE TABLE direccion (
    direccion_id SERIAL PRIMARY KEY,
    direccion_uno VARCHAR(255) NOT NULL,
    direccion_dos VARCHAR(255),
    comuna VARCHAR(100) NOT NULL,
    region VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    persona_id INT NOT NULL REFERENCES persona(persona_id)
);

-- Crear tabla tipo_telefono
CREATE TABLE tipo_telefono (
    tipo_telefono_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Crear tabla telefono
CREATE TABLE telefono (
    telefono_id SERIAL PRIMARY KEY,
    codigo_pais VARCHAR(10) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    anexo VARCHAR(10),
    tipo_telefono_id INT NOT NULL REFERENCES tipo_telefono(tipo_telefono_id),
    persona_id INT NOT NULL REFERENCES persona(persona_id)
);

-- Crear tabla profesor
CREATE TABLE profesor (
    profesor_id SERIAL PRIMARY KEY,
    asignacion VARCHAR(255) NOT NULL,
    horas_totales INT NOT NULL,
    profesor_principal BOOLEAN NOT NULL,
    persona_id INT NOT NULL REFERENCES persona(persona_id)
);

-- Crear tabla paralelo
CREATE TABLE paralelo (
    paralelo_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    numero_sala VARCHAR(10) NOT NULL
);

-- Crear tabla profesor_paralelo
CREATE TABLE profesor_paralelo (
    profesor_id INT NOT NULL REFERENCES profesor(profesor_id),
    paralelo_id INT NOT NULL REFERENCES paralelo(paralelo_id),
    creacion TIMESTAMP DEFAULT NOW(),
    anio INT NOT NULL,
    PRIMARY KEY (profesor_id, paralelo_id)
);

-- Agregue al menos 3 registros para cada tabla, considerando las relaciones.
INSERT INTO persona (nombre, apellido, fecha_nacimiento) VALUES ('Juan', 'Perez', '1990-01-01');
INSERT INTO persona (nombre, apellido, fecha_nacimiento) VALUES ('Maria', 'Gomez', '1991-02-02');
INSERT INTO persona (nombre, apellido, fecha_nacimiento) VALUES ('Pedro', 'Rodriguez', '1992-03-03');

INSERT INTO direccion (direccion_uno, direccion_dos, comuna, region, ciudad, persona_id) VALUES ('Calle 1', 'Apto 101', 'Santiago', 'Región Metropolitana', 'Santiago', 1);
INSERT INTO direccion (direccion_uno, direccion_dos, comuna, region, ciudad, persona_id) VALUES ('Calle 2', 'Apto 102', 'Valparaíso', 'Región de Valparaíso', 'Valparaíso', 2);
INSERT INTO direccion (direccion_uno, direccion_dos, comuna, region, ciudad, persona_id) VALUES ('Calle 3', 'Apto 103', 'Concepción', 'Región del Biobío', 'Concepción', 3);

INSERT INTO tipo_telefono (nombre) VALUES ('Fijo');
INSERT INTO tipo_telefono (nombre) VALUES ('Celular');
INSERT INTO tipo_telefono (nombre) VALUES ('Trabajo');

INSERT INTO telefono (codigo_pais, telefono, anexo, tipo_telefono_id, persona_id) VALUES ('+56', '999999999', '123', 1, 1);
INSERT INTO telefono (codigo_pais, telefono, anexo, tipo_telefono_id, persona_id) VALUES ('+56', '999999998', '124', 2, 2);
INSERT INTO telefono (codigo_pais, telefono, anexo, tipo_telefono_id, persona_id) VALUES ('+56', '999999997', '125', 3, 3);

INSERT INTO profesor (asignacion, horas_totales, profesor_principal, persona_id) VALUES ('Profesor de Matemáticas', 40, TRUE, 1);
INSERT INTO profesor (asignacion, horas_totales, profesor_principal, persona_id) VALUES ('Profesor de Ciencias', 35, FALSE, 2);
INSERT INTO profesor (asignacion, horas_totales, profesor_principal, persona_id) VALUES ('Profesor de Historia', 30, FALSE, 3);

INSERT INTO paralelo (nombre, numero_sala) VALUES ('Paralelo 1', '101');
INSERT INTO paralelo (nombre, numero_sala) VALUES ('Paralelo 2', '102');
INSERT INTO paralelo (nombre, numero_sala) VALUES ('Paralelo 3', '103');

INSERT INTO profesor_paralelo (profesor_id, paralelo_id, anio) VALUES (1, 1, 2025);
INSERT INTO profesor_paralelo (profesor_id, paralelo_id, anio) VALUES (2, 2, 2025);
INSERT INTO profesor_paralelo (profesor_id, paralelo_id, anio) VALUES (3, 3, 2025);

-- Obtenga lo siguiente: Direcciones por personas.
SELECT p.nombre, p.apellido, d.direccion_uno, d.direccion_dos, d.comuna, d.region, d.ciudad
FROM persona p
JOIN direccion d ON p.persona_id = d.persona_id;

-- Obtenga lo siguiente: Telefonos por personas.
SELECT p.nombre, p.apellido, t.codigo_pais, t.telefono, t.anexo, t.tipo_telefono_id
FROM persona p
JOIN telefono t ON p.persona_id = t.persona_id;

-- Obtenga lo siguiente: Profesores por paralelo.
SELECT pe.nombre, pe.apellido, pa.nombre, pa.numero_sala, pp.anio
FROM profesor p
join persona pe on pe.persona_id = p.persona_id
join profesor_paralelo pp ON p.profesor_id = pp.profesor_id
join paralelo pa on pa.paralelo_id = pp.paralelo_id;

-- Obtenga lo siguiente: Información por profesor (nombre, apellido, teléfonos, y direcciones).
SELECT pr.profesor_id, p.nombre, p.apellido, t.codigo_pais, t.telefono, t.anexo, t.tipo_telefono_id, d.direccion_uno, d.direccion_dos, d.comuna, d.region, d.ciudad
FROM persona p
join profesor pr on pr.persona_id = p.persona_id
LEFT JOIN telefono t ON p.persona_id = t.persona_id
LEFT JOIN direccion d ON p.persona_id = d.persona_id;

-- Obtenga lo siguiente: Información de paralelos de profesores, consideración todos los datos de cada persona.
SELECT p.nombre, p.apellido, pp2.paralelo_id, pp2.anio, pa.nombre, pa.numero_sala
FROM persona p
JOIN profesor pp ON p.persona_id = pp.persona_id
JOIN profesor_paralelo pp2 ON pp.profesor_id = pp2.profesor_id
JOIN paralelo pa ON pp2.paralelo_id = pa.paralelo_id;