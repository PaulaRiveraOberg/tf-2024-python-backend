-- Sistema de Gestión de Hoteles

-- Deberán aplicar más operaciones de SQL (UPDATE, DELETE, ALTER TABLE) para realizar
-- ciertas modificaciones.

-- 1. Actualizar datos:
-- Incrementa en $10.00 el precio de todas las habitaciones que pertenecen al "Hotel Sol"
UPDATE habitacion SET precio_por_noche = precio_por_noche + 10 WHERE id_hotel = 1;

-- El "Hotel Luna" ahora está ubicado en "Bosque".
UPDATE hotel SET ubicacion = 'Bosque' WHERE nombre = 'Hotel Luna';

-- Extiende la duración de la reserva de la habitación 101 en 2 días.
UPDATE reserva SET duracion = duracion + 2 WHERE id_habitacion = 1;

-- 2. Eliminar datos:
-- Borra la reserva hecha en la habitación 102.
DELETE FROM reserva WHERE id_habitacion = 2;

-- Borra todas las habitaciones cuyo precio por noche supere $120.00.
DELETE FROM habitacion WHERE precio_por_noche > 120;

-- 3. Modificar estructura:
-- Agrega una columna “estado” (tipo BOOLEAN) a la tabla “Habitacion” para indicar
-- si la habitación está disponible o no. Establece un valor por defecto en TRUE. 
ALTER TABLE habitacion ADD COLUMN estado BOOLEAN DEFAULT TRUE;

-- Cambia el tipo de dato de la columna “duracion” en la table “Reserva” para que
-- acepte decimales (por ejemplo, para medios días).
ALTER TABLE reserva ALTER COLUMN duracion TYPE NUMERIC;