
from usuario import Usuario

class Usuario_VIP(Usuario):
    def __init__(self,id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,especialidad,usuario,contraseña):
        super().__init__(id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,usuario,contraseña)
        self.especialidad=especialidad
