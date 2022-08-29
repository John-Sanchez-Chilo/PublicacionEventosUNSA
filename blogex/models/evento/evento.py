from models.evento import Evento
class Evento():
    def __init__(self,id_evento,titulo,tema,descripcion, id_encargado):
        self.id_evento = id_evento
        self.titulo = titulo
        self.tema = tema
        self.descripcion = descripcion
        self.id_encargado = id_encargado
