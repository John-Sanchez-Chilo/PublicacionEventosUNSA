/* Damos un id_usuario y verifica si es normal*/

USE UNSA;
#DROP FUNCTION esNormal;
DELIMITER $$
create definer=`root`@`localhost` function esNormal(
_id_usuario INT)RETURNS INT DETERMINISTIC
begin
    DECLARE bandera BOOL;
    DECLARE aux INT;
    
    SET bandera = (SELECT COUNT(c.id_usuario) FROM UsuarioNormal c 
        INNER JOIN  Usuario p WHERE c.id_usuario = _id_usuario AND p.id_usuario = c.id_usuario
        GROUP BY c.id_usuario);
    IF bandera THEN
       SET aux = 1;
	ELSE
       SET aux = 0;
     END IF;
    
    RETURN aux;
end$$
DELIMITER ;

#DROP FUNCTION esCliente;
USE UNSA;
SELECT* FROM Usuario;
SELECT* FROM UsuarioNormal;
SELECT esNormal(1);

/* Damos un usuario y validamos */
USE UNSA;
#DROP PROCEDURE validarLogin;
DELIMITER $$
create definer=`root`@`localhost` procedure validarLogin(
IN n_usuario varchar(30))
begin
    SELECT p.id_usuario id_usuario, p.Nombre Nombre, p.apellido_paterno, p.apellido_materno, 
           p.Correo Correo,p.Telefono Telefono, p._usuario _usuario,
           p.contrasena contra, esNormal(p.id_usuario) sies
	FROM Usuario p INNER JOIN UsuarioNormal c
    ON p._usuario = n_usuario;
    
end$$
DELIMITER ;
#DROP PROCEDURE validarLogin;
USE UNSA;
SELECT* FROM Usuario;
SELECT* FROM UsuarioNormal;
SELECT* FROM UsuarioVip;
CALL validarLogin('usuarioDos');

#Creacion de usuarios
USE UNSA;
#DROP PROCEDURE crearUsuario
DELIMITER $$
create definer=`root`@`localhost` procedure crearUsuario(
IN n_usuario varchar(30),
IN n_contrasena varchar(30),
IN n_nombre varchar(30),
IN n_apellido_paterno varchar(30),
IN n_apellido_materno varchar(30),
IN n_correo varchar(30),
IN n_telefono varchar(30),
IN n_estudios varchar(30),
IN n_descripcion varchar(30))
begin
	if (select exists (select 1 from Usuario where usuario = n_usuario)) then
		select 'Usuario ya existe!!';
	else
        insert into Usuario 
		values (null,n_usuario, n_contrasena, n_nombre, n_apellido_paterno, n_apellido_materno, n_correo, n_telefono, n_estudios,n_descripcion);
		
    end if;
end$$
DELIMITER ;

USE UNSA;
SELECT* FROM usuario;

USE UNSA;
CALL crearUsuario('usuarioTres','222','Juan','Perez','Rios','a@gmail.com','111111111','Matematica','jaansn');