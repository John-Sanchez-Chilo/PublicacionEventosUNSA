from sistema_publicacion_eventos.models.utilidad.nombre import *
class Usuario:
    def __init__(self,id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,usuario,contraseña):
        self.id_usuario=id_usuario
        self.nombre_completo=Nombre(nombre,apellido_paterno,apellido_materno)
        self.correo=correo
        self.telefono=telefono
        self.usuario=usuario
        self.contraseña=contraseña
        
    def get_nombre(self):
        return self.nombre_completo.get_nombre_completo()
