-- ---------------------------------------------------------------------------------------------------------------------
DROP DATABASE IF EXISTS deportes_de_nieve;
DROP USER IF EXISTS 'instructor'@'%';
DROP USER IF EXISTS 'alumno'@'%';
DROP USER IF EXISTS 'administrador'@'%';
DROP USER IF EXISTS 'login'@'%';
-- ---------------------------------------------------------------------------------------------------------------------
CREATE DATABASE `deportes_de_nieve` DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci;
-- ---------------------------------------------------------------------------------------------------------------------
USE `deportes_de_nieve`;
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE login (
    id smallint auto_increment,
    correo VARCHAR(50),
    contraseña VARCHAR(120),
    rol ENUM('alumno', 'instructor', 'administrador') NOT NULL,
    fecha_de_baja DATETIME,
    PRIMARY KEY (id),
    UNIQUE (correo)
);
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE actividades(
    id smallint auto_increment,
    descripcion VARCHAR(50),
    costo int,
    fecha_de_baja DATETIME,
    PRIMARY KEY (id)
);
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE equipamiento(
    id smallint auto_increment,
    id_actividad smallint,
    descripcion VARCHAR(150),
    costo int,
    PRIMARY KEY (id),
    FOREIGN KEY (id_actividad) REFERENCES actividades(id)
);
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE instructores(
    ci int,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    id_login smallint auto_increment,
    fecha_de_baja DATETIME,
    PRIMARY KEY (ci),
    FOREIGN KEY (id_login) REFERENCES login(id)
);
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE turnos(
    id smallint auto_increment,
    hora_inicio TIME,
    hora_fin TIME,
    fecha_de_baja DATETIME,
    PRIMARY KEY (id)
);
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE alumnos(
    ci int,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE,
    telefono VARCHAR(9),
    id_login smallint auto_increment,
    fecha_de_baja DATETIME,
    PRIMARY KEY (ci),
    FOREIGN KEY (id_login) REFERENCES login(id)
);
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE clase(
    id smallint auto_increment,
    ci_instructor int,
    id_actividad smallint,
    id_turno smallint,
    dictada BOOL,
    fecha_de_baja DATETIME,
    PRIMARY KEY (id),  -- Dejamos id como PRIMARY KEY
    FOREIGN KEY (ci_instructor) REFERENCES instructores(ci),
    FOREIGN KEY (id_actividad) REFERENCES actividades(id),
    FOREIGN KEY (id_turno) REFERENCES turnos(id),
    UNIQUE (ci_instructor, id_turno)  -- Un instructor no puede dar más de una clase en el mismo turno
);
-- ---------------------------------------------------------------------------------------------------------------------
CREATE TABLE alumno_clase(
    id_clase smallint,
    ci_alumno int,
    id_equipamiento smallint DEFAULT NULL,
    PRIMARY KEY (id_clase, ci_alumno),
    FOREIGN KEY (id_clase) REFERENCES clase(id),
    FOREIGN KEY (ci_alumno) REFERENCES alumnos(ci),
    FOREIGN KEY (id_equipamiento) REFERENCES equipamiento(id)
);
-- ---------------------------------------------------------------------------------------------------------------------
-- Inserción de datos en la tabla 'login', las contraseñas
INSERT INTO login (correo, contraseña, rol, fecha_de_baja) VALUES
('juan.perez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.7qqmHjQSqbbtgpPOwFh7irdybO6Fk7W', 'alumno', NULL),             -- contraseña previa al hasheo: 'passjuan123'
('maria.lopez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.J6.ta897r1gTRIo9c2a/T2Ay547.uOi', 'instructor', NULL),         -- contraseña previa al hasheo: 'passmaria456'
('carlos.gonzalez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.KoWzUHpAinSFNN9WnJegu.wq4hbeEVq', 'instructor', NULL),    -- contraseña previa al hasheo: 'passcarlos789'
('ana.ramirez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.2SYFV5N6K/sfI9EQOJBxqCe6uxQ8fDK', 'alumno', NULL),             -- contraseña previa al hasheo: 'passana001'
('pedro.martinez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.IaVAAJ8pp2kfDfQd3TtlRNRBaK878rG', 'alumno', NULL),        -- contraseña previa al hasheo: 'passpedro002'
('laura.garcia@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.6pQCAa88YHCKRvdYG5PCko2vyOZylWO', 'alumno', NULL),          -- contraseña previa al hasheo: 'passlaura003'
('jorge.lopez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.NxaoJdP9w7/Cu8hBQ1PGMcNsBMZEIyG', 'alumno', NULL),           -- contraseña previa al hasheo: 'passjorge004'
('sofia.hernandez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.ZBZvz89sj5LlfvVKHTCWvEjEGf2v4ye', 'alumno', NULL),       -- contraseña previa al hasheo: 'passsofia005'
('lucas.fernandez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.luyBU3jsL6i1SNUuHBKdwXLNRFFgRe2', 'alumno', NULL),       -- contraseña previa al hasheo: 'passlucas006'
('camila.diaz@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.4YSO3X5tkf5CPZVcFBBH4gsDh/d3OOK', 'alumno', NULL),          -- contraseña previa al hasheo: 'passcamila007'
('martin.rodriguez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.NnzDGtY.PhNa5Z/WwmWixD9izB0vek.', 'alumno', NULL),     -- contraseña previa al hasheo: 'passmartin008'
('valeria.gimenez@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.vPpkxbQsWGjmNBhPsUPTJPAigBGrUny', 'alumno', NULL),     -- contraseña previa al hasheo: 'passvaleria009'
('cristian.dinardi@ucu.edu.uy', '$2b$12$1JP0hc5vdRYqK7gLQcX1y.QJ7YfjbzFCfe5TBUoSXgY8z9sjLdxBG', 'administrador', NULL);  -- contraseña previa al hasheo: 'passcristian95'
-- ---------------------------------------------------------------------------------------------------------------------
-- Inserción de actividades
-- Inserción de actividades
INSERT INTO actividades (descripcion, costo, fecha_de_baja) VALUES
('Snowboard', 1500, NULL),
('Ski', 1700, NULL),
('Moto de nieve', 2000, NULL);
-- ---------------------------------------------------------------------------------------------------------------------
-- Inserción de equipamiento
INSERT INTO equipamiento (id_actividad, descripcion, costo) VALUES
(1, 'Kit Snowboard: lentes, tabla, traje térmico, guantes, gorro, casco', 1000),
(2, 'Kit Ski: lentes, ski y bastones, traje térmico, guantes, gorro, casco', 1200),
(3,'Kit Moto de nieve: lentes, moto de nieve, traje térmico, guantes, gorro, casco', 2000);
-- ---------------------------------------------------------------------------------------------------------------------
-- Inserción de instructores con cédulas de 8 dígitos y correo relacionado en la tabla login
INSERT INTO instructores (ci, nombre, apellido, id_login, fecha_de_baja) VALUES
(55626201, 'Juan', 'Pérez', 1, NULL),
(55626202, 'María', 'López', 2, NULL),
(55626203, 'Carlos', 'González', 3, NULL);
-- ---------------------------------------------------------------------------------------------------------------------
-- Inserción de turnos
INSERT INTO turnos (hora_inicio, hora_fin) VALUES
('09:00:00', '11:00:00'),
('12:00:00', '14:00:00'),
('16:00:00', '18:00:00');
-- ---------------------------------------------------------------------------------------------------------------------
-- Inserción de alumnos con cédulas de 8 dígitos y correo relacionado en la tabla login
INSERT INTO alumnos (ci, nombre, apellido, fecha_nacimiento, telefono, id_login, fecha_de_baja) VALUES
(55626204, 'Ana', 'Ramírez', '1995-04-10', '091234567', 4, NULL),
(55626205, 'Pedro', 'Martínez', '1998-05-15', '091234568', 5, NULL),
(55626206, 'Laura', 'García', '2000-06-20', '091234569', 6, NULL),
(55626207, 'Jorge', 'López', '1997-07-22', '091234570', 7, NULL),
(55626208, 'Sofía', 'Hernández', '1999-08-30', '091234571', 8, NULL),
(55626209, 'Lucas', 'Fernández', '1996-03-18', '091234572', 9, NULL),
(55626210, 'Camila', 'Díaz', '1998-11-09', '091234573', 10, NULL),
(55626211, 'Martín', 'Rodríguez', '2001-02-27', '091234574', 11, NULL),
(55626212, 'Valeria', 'Giménez', '1999-12-12', '091234575', 12, NULL);
-- ---------------------------------------------------------------------------------------------------------------------
-- Inserción de clases (antes de insertar en alumno_clase)
INSERT INTO clase (ci_instructor, id_actividad, id_turno, dictada, fecha_de_baja) VALUES
(55626201, 1, 1, FALSE, NULL),
(55626202, 2, 2, FALSE, NULL),
(55626203, 3, 3, FALSE, NULL),
(55626202, 1, 3, FALSE, NULL);
-- ---------------------------------------------------------------------------------------------------------------------
-- Inserción en alumno_clase
INSERT INTO alumno_clase (id_clase, ci_alumno, id_equipamiento) VALUES
(1, 55626204, 1),  -- Snowboard kit
(1, 55626205, 1),  -- Snowboard kit
(2, 55626206, 2),  -- Ski kit
(3, 55626207, 3),  -- Moto de nieve kit
(4, 55626208, 1),  -- Snowboard kit
(4, 55626209, 1),  -- Snowboard kit
(4, 55626210, 1),  -- Snowboard kit
(4, 55626211, 1),  -- Snowboard kit
(2, 55626212, 2);  -- Ski kit
-- ---------------------------------------------------------------------------------------------------------------------
CREATE OR REPLACE VIEW actividades_con_mas_alumnos AS
SELECT a.descripcion AS actividad, COUNT(ac.ci_alumno) AS total_alumnos
FROM actividades a
JOIN clase c ON a.id = c.id_actividad
JOIN alumno_clase ac ON c.id = ac.id_clase
WHERE a.fecha_de_baja IS NULL AND c.fecha_de_baja IS NULL
GROUP BY a.descripcion
ORDER BY total_alumnos DESC;

CREATE OR REPLACE VIEW turnos_con_mas_clases_dictadas AS
SELECT t.hora_inicio, t.hora_fin, COUNT(c.id) AS total_clases
FROM turnos t
JOIN clase c ON t.id = c.id_turno
WHERE t.fecha_de_baja IS NULL AND c.fecha_de_baja IS NULL
GROUP BY t.hora_inicio, t.hora_fin
ORDER BY total_clases DESC;

CREATE OR REPLACE VIEW actividades_que_mas_ingresos_generan AS
SELECT a.descripcion AS actividad, SUM(a.costo + IFNULL(e.costo, 0)) AS total_ingresos
FROM actividades a
JOIN clase c ON a.id = c.id_actividad
JOIN alumno_clase ac ON c.id = ac.id_clase
LEFT JOIN equipamiento e ON ac.id_equipamiento = e.id
WHERE a.fecha_de_baja IS NULL AND c.fecha_de_baja IS NULL
GROUP BY a.descripcion
ORDER BY total_ingresos DESC;
-- ---------------------------------------------------------------------------------------------------------------------
CREATE EVENT actualizar_dictada
ON SCHEDULE EVERY 1 MINUTE
DO
BEGIN
    UPDATE clase AS c
    JOIN turnos AS t ON c.id_turno = t.id
    SET c.dictada = (
        CASE
            WHEN TIME(NOW()) BETWEEN t.hora_inicio AND t.hora_fin THEN TRUE
            ELSE FALSE
        END
    )
    WHERE c.fecha_de_baja IS NULL AND t.fecha_de_baja IS NULL;
END;

SET GLOBAL event_scheduler = ON;
-- ---------------------------------------------------------------------------------------------------------------------
-- Crear usuarios adicionales para '%'
CREATE USER 'administrador'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'AAJ-394monoia';
GRANT ALL PRIVILEGES ON deportes_de_nieve.* TO 'administrador'@'%';

CREATE USER 'alumno'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'Estudio231564';
GRANT SELECT, INSERT, UPDATE, DELETE ON deportes_de_nieve.alumno_clase TO 'alumno'@'%';
GRANT SELECT ON deportes_de_nieve.turnos TO 'alumno'@'%';
GRANT SELECT ON deportes_de_nieve.actividades TO 'alumno'@'%';
GRANT SELECT ON deportes_de_nieve.clase TO 'alumno'@'%';
GRANT SELECT ON deportes_de_nieve.alumnos TO 'alumno'@'%';

CREATE USER 'instructor'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'Instruc_najuale';
GRANT SELECT, INSERT, DELETE ON deportes_de_nieve.alumno_clase TO 'instructor'@'%';
GRANT SELECT ON deportes_de_nieve.clase TO 'instructor'@'%';
GRANT SELECT ON deportes_de_nieve.turnos TO 'instructor'@'%';
GRANT SELECT ON deportes_de_nieve.actividades TO 'instructor'@'%';
GRANT SELECT ON deportes_de_nieve.alumnos TO 'instructor'@'%';

CREATE USER 'login'@'%' IDENTIFIED WITH 'mysql_native_password' BY 'LogDepNev2024JAI';
GRANT SELECT ON deportes_de_nieve.login TO 'login'@'%';
GRANT SELECT ON deportes_de_nieve.alumnos TO 'login'@'%';
GRANT SELECT ON deportes_de_nieve.instructores TO 'login'@'%';
FLUSH PRIVILEGES;
