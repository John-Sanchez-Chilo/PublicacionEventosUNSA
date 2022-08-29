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
