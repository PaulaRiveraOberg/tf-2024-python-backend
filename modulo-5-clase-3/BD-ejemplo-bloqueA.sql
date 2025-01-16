-- Crear la tabla 'estudiante'
CREATE TABLE IF NOT EXISTS estudiante (
    id_estudiante SERIAL PRIMARY KEY,
    rut_estudiante VARCHAR UNIQUE,
    nombre_estudiante VARCHAR NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    direccion VARCHAR,
    correo VARCHAR,
    telefono VARCHAR
);

-- Crear la tabla 'programa'
CREATE TABLE IF NOT EXISTS programa (
    id_programa SERIAL PRIMARY KEY,
    nombre_programa VARCHAR NOT NULL,
    cantidad_horas INTEGER NOT NULL
);

-- Crear la tabla 'modulo'
CREATE TABLE IF NOT EXISTS modulo (
    id_modulo SERIAL PRIMARY KEY,
    nombre_modulo VARCHAR NOT NULL,
    cantidad_horas INTEGER NOT NULL,
    id_programa INTEGER NOT NULL,
    FOREIGN KEY (id_programa) REFERENCES programa(id_programa)
);

-- Crear la tabla 'relator'
CREATE TABLE IF NOT EXISTS relator (
    id_relator SERIAL PRIMARY KEY,
    rut_relator VARCHAR UNIQUE,
    nombre_relator VARCHAR NOT NULL,
    titulo_relator VARCHAR,
    anios_experiencia INTEGER,
    valor_hora INTEGER
);

-- Crear la tabla 'curso'
CREATE TABLE IF NOT EXISTS curso (
    id_curso SERIAL PRIMARY KEY,
    codigo_curso VARCHAR UNIQUE NOT NULL,
    cantidad_estudiantes INTEGER NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_termino DATE NOT NULL,
    id_programa INTEGER NOT NULL,
    FOREIGN KEY (id_programa) REFERENCES programa(id_programa)
);

-- Crear la tabla 'estudiante_curso' (relación muchos a muchos entre estudiante y curso)
CREATE TABLE IF NOT EXISTS estudiante_curso (
    id_estudiante INTEGER NOT NULL,
    id_curso INTEGER NOT NULL,
    PRIMARY KEY (id_estudiante, id_curso),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante) ON DELETE CASCADE,
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso) ON DELETE CASCADE
);

-- Crear la tabla 'relator_modulo' (relación muchos a muchos entre relator y módulo)
CREATE TABLE IF NOT EXISTS relator_modulo (
    id_relator INTEGER NOT NULL,
    id_modulo INTEGER NOT NULL,
    PRIMARY KEY (id_relator, id_modulo),
    FOREIGN KEY (id_relator) REFERENCES relator(id_relator) ON DELETE CASCADE,
    FOREIGN KEY (id_modulo) REFERENCES modulo(id_modulo) ON DELETE CASCADE
);

-- Ejemplos de inserción

-- Tabla 'estudiante'
INSERT INTO estudiante (rut_estudiante, nombre_estudiante, fecha_nacimiento, direccion, correo, telefono) VALUES
('12345678-9', 'Juan Pérez', '2000-01-15', 'Calle Falsa 123', 'juan.perez@example.com', '912345678'),
('87654321-0', 'María López', '1998-07-23', 'Av. Siempreviva 456', 'maria.lopez@example.com', '987654321');

-- Tabla 'programa'
INSERT INTO programa (nombre_programa, cantidad_horas) VALUES
('Ingeniería en Informática', 3600),
('Diseño Gráfico', 1800), 
('Ingeniería Comercial', 1600);
-- Tabla 'modulo'
INSERT INTO modulo (nombre_modulo, cantidad_horas, id_programa) VALUES
('Programación Avanzada', 120, 1),
('Bases de Datos', 90, 1),
('Diseño Web', 80, 2);

-- Tabla 'relator'
INSERT INTO relator (rut_relator, nombre_relator, titulo_relator, anios_experiencia, valor_hora) VALUES
('23456789-1', 'Carlos Ruiz', 'Ingeniero Informático', 10, 25000),
('34567891-2', 'Ana Fernández', 'Diseñadora Gráfica', 8, 20000);

-- Tabla 'curso'
INSERT INTO curso (codigo_curso, cantidad_estudiantes, fecha_inicio, fecha_termino, id_programa) VALUES
('INF-2024-01', 25, '2024-03-01', '2024-06-30', 1),
('DG-2024-01', 20, '2024-04-01', '2024-07-31', 2);

-- Tabla 'estudiante_curso'
INSERT INTO estudiante_curso (id_estudiante, id_curso) VALUES
(1, 1),
(2, 2);

-- Tabla 'relator_modulo'
INSERT INTO relator_modulo (id_relator, id_modulo) VALUES
(1, 1),
(2, 3);

