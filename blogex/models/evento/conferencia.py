from models.evento import Evento
class Conferencia(Evento):
    def __init__(self,id_evento,titulo,tema,descripcion, id_encargado,id_evento_conferencia,fecha, hora):
        super().__init__(id_evento,titulo,tema,descripcion, id_encargado)
        self.id_evento_conferencia = id_evento_conferencia
        self.fecha = fecha
        self.hora = hora
