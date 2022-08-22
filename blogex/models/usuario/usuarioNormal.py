
from usuario import Usuario
class Usuario_Normal(Usuario):
    def __init__(self,id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,centro_estudios,usuario,contraseña):
        super().__init__(id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,usuario,contraseña)
        self.centro_estudios=centro_estudios
