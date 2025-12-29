CREATE DATABASE IF NOT EXISTS moche_db;
USE moche_db;

CREATE TABLE IF NOT EXISTS roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);


CREATE TABLE IF NOT EXISTS datos_del_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre_del_usuario VARCHAR(50),
    email_del_usuario VARCHAR(100),
    contraseña_del_usuario VARCHAR(255),
    roles_id INT,
    FOREIGN KEY (roles_id) REFERENCES roles(id)
);


CREATE TABLE IF NOT EXISTS proyectos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_del_proyecto VARCHAR (50) NOT NULL,
    descripcion_del_proyecto VARCHAR (255),
    imagen VARCHAR(255),
    link_del_proyecto VARCHAR(2048) NOT NULL,
    fecha_de_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES datos_del_usuario(id)
)