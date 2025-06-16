-- Repartido 2
-- ---------------------------------------------------------------------------------------------------------------------
-- Copy Paste
create table producto(idproducto varchar(20) primary key,
                     nombreproducto varchar(20),
                     preciounitario varchar(20));
insert into usuario values ('pperez', 'Pedro', 'Perez', '2004/01/20' );
-- ---------------------------------------------------------------------------------------------------------------------
-- Los tablas necesarias con sus respectivos datos
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE Usuario (
    nombreUsuario VARCHAR(50) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    fechaNacimiento DATE
);
CREATE TABLE Producto (
    idProducto INT PRIMARY KEY,
    nombreProducto VARCHAR(100) NOT NULL,
    precioUnitario DECIMAL(10, 2) NOT NULL
);
CREATE TABLE Pedido (
    idPedido INT PRIMARY KEY,
    fechaSolicitud DATE NOT NULL,
    nombreUsuario VARCHAR(50),
    FOREIGN KEY (nombreUsuario) REFERENCES Usuario(nombreUsuario)
);
CREATE TABLE ProductoPedido (
    idPedido INT,
    idProducto INT,
    cantidad INT NOT NULL,
    PRIMARY KEY (idPedido, idProducto),
    FOREIGN KEY (idPedido) REFERENCES Pedido(idPedido),
    FOREIGN KEY (idProducto) REFERENCES Producto(idProducto)
);
INSERT INTO Usuario VALUES ('pperez', 'Pedro', 'Perez', 'password1', '2004/01/20');
INSERT INTO Usuario VALUES ('lgomez', 'Laura', 'Gomez', 'password2', '1999/05/12');
INSERT INTO Usuario VALUES ('dgarcia', 'Daniel', 'Garcia', 'password3', '1990/10/30');
INSERT INTO Usuario VALUES ('asanchez', 'Ana', 'Sanchez', 'password4', '1988/11/22');
INSERT INTO Usuario VALUES ('mbenitez', 'Marcos', 'Benitez', 'password5', '1995/09/18');
INSERT INTO Usuario VALUES ('jmartinez', 'Jorge', 'Martinez', 'password6', '2002/12/05');
INSERT INTO Usuario VALUES ('acarvajal', 'Alicia', 'Carvajal', 'password7', '2000/07/14');
INSERT INTO Usuario VALUES ('jperez', 'Jose', 'Perez', 'password8', '1997/02/28');
INSERT INTO Usuario VALUES ('rlopez', 'Ricardo', 'Lopez', 'password9', '1993/04/08');
INSERT INTO Usuario VALUES ('ssilva', 'Sandra', 'Silva', 'password10', '1991/03/17');

INSERT INTO Producto VALUES (1, 'Laptop', 750.00);
INSERT INTO Producto VALUES (2, 'Mouse', 20.00);
INSERT INTO Producto VALUES (3, 'Teclado', 45.00);
INSERT INTO Producto VALUES (4, 'Monitor', 200.00);
INSERT INTO Producto VALUES (5, 'Impresora', 150.00);
INSERT INTO Producto VALUES (6, 'Auriculares', 35.00);
INSERT INTO Producto VALUES (7, 'Webcam', 70.00);
INSERT INTO Producto VALUES (8, 'Disco Duro', 85.00);
INSERT INTO Producto VALUES (9, 'Memoria USB', 15.00);
INSERT INTO Producto VALUES (10, 'Cargador de Iphone', 25.00);

INSERT INTO Pedido VALUES (101, '2024/09/01', 'pperez');
INSERT INTO Pedido VALUES (102, '2024/09/02', 'lgomez');
INSERT INTO Pedido VALUES (103, '2024/09/03', 'dgarcia');
INSERT INTO Pedido VALUES (104, '2024/09/04', 'asanchez');
INSERT INTO Pedido VALUES (105, '2024/09/05', 'mbenitez');
INSERT INTO Pedido VALUES (106, '2024/09/06', 'jmartinez');
INSERT INTO Pedido VALUES (107, '2024/09/07', 'acarvajal');
INSERT INTO Pedido VALUES (108, '2024/09/08', 'jperez');
INSERT INTO Pedido VALUES (109, '2024/09/09', 'rlopez');
INSERT INTO Pedido VALUES (110, '2024/09/10', 'ssilva');

INSERT INTO ProductoPedido VALUES (101, 1, 1);  -- Pedido 101: 1 Laptop
INSERT INTO ProductoPedido VALUES (101, 2, 2);  -- Pedido 101: 2 Mouse
INSERT INTO ProductoPedido VALUES (102, 3, 1);  -- Pedido 102: 1 Teclado
INSERT INTO ProductoPedido VALUES (103, 4, 1);  -- Pedido 103: 1 Monitor
INSERT INTO ProductoPedido VALUES (104, 5, 1);  -- Pedido 104: 1 Impresora
INSERT INTO ProductoPedido VALUES (105, 6, 1);  -- Pedido 105: 1 Auriculares
INSERT INTO ProductoPedido VALUES (106, 7, 1);  -- Pedido 106: 1 Webcam
INSERT INTO ProductoPedido VALUES (107, 8, 1);  -- Pedido 107: 1 Disco Duro
INSERT INTO ProductoPedido VALUES (108, 9, 3);  -- Pedido 108: 3 Memorias USB
INSERT INTO ProductoPedido VALUES (109, 10, 1); -- Pedido 109: 1 Cargador de Iphone
-- ---------------------------------------------------------------------------------------------------------------------
-- Obtener el usuario con la mayor cantidad de pedidos
-- ---------------------------------------------------------------------------------------------------------------------
SELECT nombreUsuario, COUNT(*) AS cantidadPedidos
FROM Pedido
GROUP BY nombreUsuario
ORDER BY cantidadPedidos DESC
LIMIT 1;
-- ---------------------------------------------------------------------------------------------------------------------
-- Obtener el producto más vendido
-- ---------------------------------------------------------------------------------------------------------------------
SELECT idProducto, SUM(cantidad) AS cantidadVendida
FROM ProductoPedido
GROUP BY idProducto
ORDER BY cantidadVendida DESC
LIMIT 1;
-- ---------------------------------------------------------------------------------------------------------------------
-- Obtener el costo total del pedido con id = 10.
-- ---------------------------------------------------------------------------------------------------------------------
SELECT SUM(P.precioUnitario * PP.cantidad) AS costoTotal
FROM Producto P
JOIN ProductoPedido PP ON P.idProducto = PP.idProducto
WHERE PP.idPedido = 10;
-- ---------------------------------------------------------------------------------------------------------------------
--  Obtener los productos que compra el usuario ‘srochet’.
SELECT P.nombreProducto
FROM Producto P
JOIN ProductoPedido PP ON P.idProducto = PP.idProducto
JOIN Pedido Pe ON PP.idPedido = Pe.idPedido
WHERE Pe.nombreUsuario = 'srochet';
-- ---------------------------------------------------------------------------------------------------------------------
-- Parte 3
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE NotasTarea (
    fechaTarea DATE,
    nombreTarea VARCHAR(100),
    tipoTarea VARCHAR(50),
    notaTarea DECIMAL(5,2),
    PRIMARY KEY (fechaTarea, nombreTarea),
    FOREIGN KEY (tipoTarea) REFERENCES Tarea(tipoTarea)
);
INSERT INTO Tarea VALUES ('Quizzes, Kahoot', 0.05, NULL);
INSERT INTO Tarea VALUES ('Prácticos y trabajos de inv.', 0.10, 8);
INSERT INTO Tarea VALUES ('Obligatorio', 0.35, 1);
INSERT INTO Tarea VALUES ('Parciales', 0.50, 2);

INSERT INTO NotasTarea VALUES ('2023-09-01', 'Quiz 1', 'Quizzes, Kahoot', 8.45);
INSERT INTO NotasTarea VALUES ('2023-09-05', 'Parcial 1', 'Parciales', 7.50);
-- Y así sucesivamente para otras tareas

SELECT T.tipoTarea, N.notaTarea, T.ponderacion,
       (N.notaTarea * T.ponderacion) AS contribucion
FROM NotasTarea N
JOIN Tarea T ON N.tipoTarea = T.tipoTarea;

SELECT SUM(N.notaTarea * T.ponderacion) AS porcentajeAprobacion
FROM NotasTarea N
JOIN Tarea T ON N.tipoTarea = T.tipoTarea;
-- ---------------------------------------------------------------------------------------------------------------------
-- Fin :) Juan Paroli
-- ---------------------------------------------------------------------------------------------------------------------
