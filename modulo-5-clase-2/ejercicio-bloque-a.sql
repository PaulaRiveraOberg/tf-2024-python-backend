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