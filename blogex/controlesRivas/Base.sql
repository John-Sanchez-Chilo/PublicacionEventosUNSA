CREATE DATABASE UNSA;
#DROP DATABASE UNSA;
USE UNSA;
CREATE TABLE Usuario(#persona
	id_usuario INT AUTO_INCREMENT UNIQUE,
    Nombre VARCHAR(30) ,
    ApellidoPaterno VARCHAR(30) ,
    ApellidoMaterno VARCHAR(30) ,
    Correo VARCHAR(30),
    Telefono VARCHAR(30),
    _usuario varchar(30), 
    contra VARCHAR(30) ,
    Estudios VARCHAR(30) ,
    Descripcion VARCHAR(30) ,
    PRIMARY KEY(id_usuario)
);
CREATE TABLE UsuarioNormal(#cliente
	id_usuario INT ,
	saldo DECIMAL(5,2) NOT NULL,
	foreign key(id_usuario) references Usuario(id_usuario),
    primary key(id_usuario)
);
CREATE TABLE UsuarioVip(#vendedor
	id_usuario INT ,
	sueldo DECIMAL(5,2) NOT NULL,
	foreign key(id_usuario) references Usuario(id_usuario),
	primary key(id_usuario)
);
/*Insertando Usuario id_usuario ,Nombre ,ApellidoPaterno ,ApellidoMaterno ,Correo ,Telefono ,usuario , contra ,
    Estudios ,
    Descripcion , */
USE unsa;
INSERT INTO Usuario 
VALUES(NULL,'Diego','Rios','Valdivia','asd@gmail.com','976826912','usuarioUno','123','Computacion','Estudiante Promedio');

INSERT INTO Usuario 
VALUES(NULL,'Raul','Ventura','Valdivia','rfg@gmail.com','972326912','usuarioDos','321','Biologia','Estudiante Excepcional');


#usuario normal
INSERT INTO UsuarioNormal
VALUES(1,350.00);
#usuario vip
INSERT INTO UsuarioVip
VALUES(2,250.00);

select* from Usuario;
select* from UsuarioNormal;
select* from UsuarioVip;