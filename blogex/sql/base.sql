CREATE DATABASE UNSA;
USE UNSA;
CREATE TABLE Usuario(#persona
	id_usuario INT auto_increment unique,
    usuario VARCHAR(30),
    contrasena VARCHAR(30),
    nombre VARCHAR(30) ,
    apellido_paterno VARCHAR(30) ,
    apellido_materno VARCHAR(30) ,
    correo VARCHAR(30),
    telefono VARCHAR(30),
    estudios VARCHAR(30) ,
    descripcion VARCHAR(30) ,
    PRIMARY KEY(id_usuario)
);

CREATE TABLE UsuarioNormal(#cliente
	id_usuario INT ,
	#saldo DECIMAL(5,2) NOT NULL,
	foreign key(id_usuario) references Usuario(id_usuario),
    primary key(id_usuario)
);
CREATE TABLE UsuarioVip(#vendedor
	id_usuario INT ,
	especialidad VARCHAR(30),
	foreign key(id_usuario) references Usuario(id_usuario),
	primary key(id_usuario)
);
CREATE TABLE Evento(
    id_evento INT,
    titulo VARCHAR(30),
    tema VARCHAR(30) ,
    descripcion VARCHAR(30) ,
    id_encargado INT,
    primary key (id_evento),
    foreign key(id_encargado) references Usuario(id_usuario)
);
CREATE TABLE Conferencia(
    id_evento_conferencia INT,
    fecha DATE,
    hora TIME,
    primary key (id_evento_conferencia),
    foreign key(id_evento_conferencia) references Evento(id_evento)
);
CREATE TABLE Workshop(
    id_evento_workshop INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    primary key (id_evento_workshop),
    foreign key(id_evento_workshop) references Evento(id_evento)
);
CREATE TABLE Simposio(
    id_evento_simposio INT,
    fecha DATE,
    hora TIME,
    primary key (id_evento_simposio),
    foreign key(id_evento_simposio) references Evento(id_evento)
);
CREATE TABLE Propuesta(
    id_propuesta INT auto_increment unique,
    titulo VARCHAR(30) ,
    tema VARCHAR(30) ,
    descripcion VARCHAR(200) ,
    tipo VARCHAR(30) ,
    id_usuario_encargado INT ,
    primary key (id_propuesta),
    foreign key(id_usuario_encargado) references Usuario(id_usuario)
);
CREATE TABLE Coordinador(
    id_coordinador INT,
    nombre VARCHAR(30),
    especialidad VARCHAR(30),
    primary key (id_coordinador)
);
CREATE TABLE Administrador(
    id_admin VARCHAR(30) ,
    nombre VARCHAR(30) ,
    primary key (id_admin)
);

INSERT INTO Usuario 
VALUES(NULL,'usuarioUno','123','Diego','Rios','Valdivia','asd@gmail.com','976826912','Computacion','Estudiante Promedio');

INSERT INTO Usuario 
VALUES(NULL,'usuarioDos','321','Raul','Ventura','Valdivia','rfg@gmail.com','972326912','Biologia','Estudiante Excepcional');

Insert into Propuesta 
values (null, 'Expasion de grafos','Grafos','Pienso hacer una exposicion resumiendo las entasjde utiliza grafos ys sus beneificos en trabajo','Conferencia',1);