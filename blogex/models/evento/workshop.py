from models.evento import Evento
class Workshop(Evento):
    def __init__(self,id_evento,titulo,tema,descripcion, id_encargado,id_evento_conferencia,fecha_inicio, fecha_fin):
        super().__init__(id_evento,titulo,tema,descripcion, id_encargado)
        self.id_evento_conferencia = id_evento_conferencia
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
