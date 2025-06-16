use practico1;

CREATE TABLE personas (
	email VARCHAR(50) NOT NULL,
    password VARCHAR(20),
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    fecha_nacimiento DATE,
    PRIMARY KEY (email)
);

CREATE TABLE tipo_videojuegos (
	tipo VARCHAR(50) NOT NULL,
    PRIMARY KEY (tipo)
);

CREATE TABLE videojuegos (
	nombre VARCHAR(50) NOT NULL,
	dificultad varchar (50) CHECK (dificultad IN ('1', '2', '3','4','5')),
    descripcion VARCHAR(200),
    costo SMALLINT,
    tipo VARCHAR(50),
    PRIMARY KEY (nombre),
    FOREIGN KEY (tipo) REFERENCES tipo_videojuegos(tipo)
);

CREATE TABLE expansiones (
	nombre VARCHAR (50) NOT NULL,
    nombre_videojuego VARCHAR(50),
    costo SMALLINT,
    PRIMARY KEY (nombre, nombre_videojuego),
    FOREIGN KEY (nombre_videojuego) REFERENCES videojuegos(nombre)
);


CREATE TABLE compra (
	email VARCHAR(50) NOT NULL,
    nombre_videojuego VARCHAR(50) NOT NULL,
    nombre_expansion VARCHAR(50) NOT NULL,
    valor SMALLINT,
    fecha date NOT NULL,
    PRIMARY KEY (email, nombre_videojuego, fecha),
    FOREIGN KEY (nombre_videojuego) REFERENCES videojuegos(nombre),
    FOREIGN KEY (nombre_expansion,nombre_videojuego) REFERENCES expansiones(nombre, nombre_videojuego)
);

CREATE TABLE juega (
	email VARCHAR(50) NOT NULL,
    nombre_videojuego VARCHAR(50) NOT NULL,
    fecha date,
    PRIMARY KEY (email, nombre_videojuego, fecha),
    FOREIGN KEY (email) REFERENCES personas(email),
    FOREIGN KEY (nombre_videojuego) REFERENCES videojuegos(nombre)
);

CREATE TABLE amigos (
	email_persona VARCHAR(50) NOT NULL,
    email_amigo VARCHAR(50) NOT NULL,
    PRIMARY KEY (email_persona, email_amigo),
    FOREIGN KEY (email_persona) REFERENCES personas(email),
    FOREIGN KEY (email_amigo) REFERENCES personas(email)
);

USE practico1;

INSERT INTO personas(email, nombre, apellido, fecha_nacimiento) VALUES 
('persona1@gmail.com', 'Alejandro', 'Ben�tez', '2010-10-01'),
('persona2@gmail.com', 'Martina', 'Castro', '2009-10-01'),
('persona3@gmail.com', 'Daniel', 'D�az', '2010-12-01'),
('persona4@gmail.com', 'Patricia', 'P�rez', '2004-10-01'),
('persona5@gmail.com', 'Mateo', 'Rodr�guez', '2004-12-01'),
('persona6@gmail.com', 'Gimena', 'Garc�a', '2000-10-01'),
('persona7@gmail.com', 'Sergio', 'de Le�n', '1998-10-01'),
('persona8@gmail.com', 'Fernanda', 'Mu�oz', '1990-10-01'),
('persona9@gmail.com', 'Gonzalo', 'Pereira', '1980-10-01'),
('persona10@gmail.com', 'Mercedes', 'Ferreira', '2005-10-01');

INSERT INTO amigos(email_persona, email_amigo) VALUES
('persona1@gmail.com', 'persona2@gmail.com'),
('persona1@gmail.com', 'persona3@gmail.com'),
('persona2@gmail.com', 'persona4@gmail.com'),
('persona2@gmail.com', 'persona5@gmail.com'),
('persona2@gmail.com', 'persona6@gmail.com'),
('persona3@gmail.com', 'persona1@gmail.com'),
('persona9@gmail.com', 'persona8@gmail.com'),
('persona9@gmail.com', 'persona1@gmail.com'),
('persona8@gmail.com', 'persona6@gmail.com');


INSERT INTO tipo_videojuegos(tipo) VALUES 
('cartas'), 
('shooter'),
('estrategia'), 
('simulacion'), 
('rpg');


INSERT INTO videojuegos(nombre, dificultad, descripcion, costo, tipo) VALUES 
('Project Zomboid', '3', 'Project Zomboid is the ultimate in zombie survival. Alone or in MP: you loot, build, craft, fight, farm and fish in a struggle to survive',  429, 'rpg'), 
('Tower of Fantasy', '2', 'Embark together on your fantasy adventure! Set hundreds of years in the future on the distant planet of Aida, the shared open-world RPG, anime-infused sci-fi adventure', 0, 'rpg'),
('Magic: The Gathering Arena', '3', 'Juego digital de cartas coleccionables desarrollado y publicado por Wizards of the Coast', 0, 'cartas'), 
('Battlefield 2042', '5', 'Battlefield 2042 es un shooter en primera persona que marca el regreso a la emblem�tica guerra total de la franquicia.', 2600,  'cartas');

INSERT INTO expansiones(nombre, nombre_videojuego, costo) VALUES 
('Battlefield 2042 Ultimate Edition', 'Battlefield 2042', 4800);

INSERT INTO compra (email, nombre_videojuego, nombre_expansion, valor, fecha) VALUES
('persona3@gmail.com', 'Battlefield 2042', 'Battlefield 2042 Ultimate Edition', 7400, '2024-03-22');

INSERT INTO juega (email, nombre_videojuego, fecha) VALUES
('persona1@gmail.com', 'Project Zomboid', '2024-01-20'),
('persona2@gmail.com', 'Tower of Fantasy', '2024-02-15'),
('persona3@gmail.com', 'Battlefield 2042', '2024-03-25');




