-- UPDATE permite modificar los datos de una tabla
UPDATE producto SET precio = 29.99 WHERE id = 1;

-- DELETE permite eliminar los datos de una tabla
DELETE FROM transaccion WHERE id_transaccion = 3;

-- Para modificar la tabla usamos ALTER TABLE
-- para agregar una columna
ALTER TABLE producto ADD COLUMN stock int DEFAULT 0;

-- para modificar una columna
ALTER TABLE transaccion ALTER COLUMN cantidad TYPE NUMERIC;

-- para eliminar una columna
ALTER TABLE producto DROP COLUMN stock;