from models.Evento import Evento
class Propuesta(object):
    def __init__(self,id_propuesta=None, titulo=None, descripcion=None, tema=None,):
        self.id_propuesta = id_propuesta
        self.titulo = titulo
        self.descripcion = descripcion
        self.tema = tema

    #funcion para pasar una propuesta aceptada a un evento ascociando al encargado
    def convertir_a_evento(self,encargado):
        evento=Evento(self.id_propuesta,self.titulo,self.descripcion,encargado,self.tema)
        return evento
