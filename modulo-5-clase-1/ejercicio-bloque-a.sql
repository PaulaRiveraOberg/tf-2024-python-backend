-- Sistema de Gestión de Hoteles

-- Una cadena hotelera necesita gestionar información sobre sus hoteles, las habitaciones
-- disponibles y las reservas realizadas. Para ello deberán modelar esta información en una
-- base de datos PostgreSQL y realizar consultas básicas.

-- Instrucciones:
-- 1. Configurar entorno local PostgreSQL y crear base de datos.
CREATE DATABASE hoteles;
-- 2. Crear las tablas
CREATE TABLE hotel (
    id_hotel serial primary key,
    nombre varchar(50),
    ubicacion varchar(100)
);

CREATE TABLE habitacion (
    id_habitacion serial primary key,
    id_hotel int references hotel(id_hotel),
    numero int,
    precio_por_noche decimal(10, 2)
);

CREATE TABLE reserva (
    id_reserva serial primary key,
    id_habitacion int references habitacion(id_habitacion),
    fecha_reserva date,
    duracion int
);
-- 3. Insertar datos
-- hoteles
INSERT INTO hotel (nombre, ubicacion) VALUES ('Hotel Sol', 'Playa');
INSERT INTO hotel (nombre, ubicacion) VALUES ('Hotel Luna', 'Montaña');
-- habitaciones
INSERT INTO habitacion (id_hotel, numero, precio_por_noche) VALUES (1, 101, 100);
INSERT INTO habitacion (id_hotel, numero, precio_por_noche) VALUES (1, 102, 120);
INSERT INTO habitacion (id_hotel, numero, precio_por_noche) VALUES (2, 201, 80);
INSERT INTO habitacion (id_hotel, numero, precio_por_noche) VALUES (2, 202, 95);
-- reservas
INSERT INTO reserva (id_habitacion, fecha_reserva, duracion) VALUES (1, '2024-12-01', 3);
INSERT INTO reserva (id_habitacion, fecha_reserva, duracion) VALUES (2, '2024-12-02', 2);
INSERT INTO reserva (id_habitacion, fecha_reserva, duracion) VALUES (3, '2024-01-03', 1);

-- 4. Consultar los datos
-- ¿Cuáles son los nombres y ubicaciones de todos los hoteles registrados?
SELECT nombre, ubicacion FROM hotel;
-- ¿Qué información hay sobre todas las habitaciones registradas?
SELECT * FROM habitacion;
-- ¿Cuáles son las habitaciones cuyo precio por noche es mayor a $90.00?
SELECT * FROM habitacion WHERE precio_por_noche > 90;
-- ¿Cuál es la duración total de todas las reservas realizadas?
SELECT SUM(duracion) FROM reserva;