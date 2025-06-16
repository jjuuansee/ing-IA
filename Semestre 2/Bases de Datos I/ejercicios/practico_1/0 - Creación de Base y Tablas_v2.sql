DROP DATABASE IF EXISTS `practico1`;

CREATE DATABASE `practico1` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci;

CREATE TABLE practico1.personas (
	email VARCHAR(50) NOT NULL,
    password VARCHAR(20),
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    fecha_nacimiento DATE,
    PRIMARY KEY (email)
);

CREATE TABLE practico1.tipo_videojuegos (
	tipo VARCHAR(50) NOT NULL,
    PRIMARY KEY (tipo)
);

CREATE TABLE practico1.videojuegos (
	nombre VARCHAR(50) NOT NULL,
	dificultad ENUM('1', '2', '3', '4', '5'),
    descripcion VARCHAR(200),
    costo SMALLINT,
    tipo VARCHAR(50),
    PRIMARY KEY (nombre),
    FOREIGN KEY (tipo) REFERENCES tipo_videojuegos(tipo)
);

CREATE TABLE practico1.expansiones (
	nombre VARCHAR (50) NOT NULL,
    nombre_videojuego VARCHAR(50) NOT NULL,
    costo SMALLINT,
    PRIMARY KEY (nombre, nombre_videojuego),
    FOREIGN KEY (nombre_videojuego) REFERENCES videojuegos(nombre)
);

CREATE TABLE practico1.amigos (
	email_persona VARCHAR(50) NOT NULL,
    email_amigo VARCHAR(50) NOT NULL,
    PRIMARY KEY (email_persona, email_amigo),
    FOREIGN KEY (email_persona) REFERENCES personas(email),
    FOREIGN KEY (email_amigo) REFERENCES personas(email)
);

CREATE TABLE practico1.compra (
	email VARCHAR(50) NOT NULL,
    nombre_videojuego VARCHAR(50) NOT NULL,
    nombre_expansion VARCHAR(50) ,
    valor SMALLINT,
    fecha date NOT NULL,
    PRIMARY KEY (email, nombre_videojuego, fecha),
    FOREIGN KEY (nombre_videojuego) REFERENCES videojuegos(nombre),
    FOREIGN KEY (nombre_expansion) REFERENCES expansiones(nombre)
);

CREATE TABLE practico1.juega (
	email VARCHAR(50) NOT NULL,
    nombre_videojuego VARCHAR(50) NOT NULL,
    fecha date,
    PRIMARY KEY (email, nombre_videojuego, fecha),
    FOREIGN KEY (email) REFERENCES personas(email),
    FOREIGN KEY (nombre_videojuego) REFERENCES videojuegos(nombre)
);

