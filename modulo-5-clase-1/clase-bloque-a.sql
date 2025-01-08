-- creación de una tabla
create table categoria (
    id serial primary key,
    nombre varchar(50),
);

create table producto (
    id serial primary key,
    nombre varchar(50),
    id_categoria int references categoria(id),
    precio decimal(10, 2),
);

create table transaccion (
    id_transaccion serial primary key,
    id_producto int references producto(id),
    fecha date,
    cantidad int,
);

-- inserción de datos
insert into categoria (nombre) values ('Electrónica');
insert into categoria (nombre) values ('Muebles');

insert into producto (nombre, id_categoria, precio) values ('Laptop', 1, 1000);
insert into producto (nombre, id_categoria, precio) values ('Silla', 2, 50);
insert into producto (nombre, id_categoria, precio) values ('Mesa', 2, 100);

-- ver datos de las tablas
select * from categoria;
select * from producto;
select * from transaccion;

-- seleccionar usando where
select * from producto where id_categoria = 1;
select * from transaccion where id_producto = 1;
select * from producto where precio > 100;


