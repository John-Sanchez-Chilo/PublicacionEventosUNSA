
class Horario:
    def __init__(self,hora,minuto):
        self.hora = hora
        self.minuto = minuto
    
    def get_horario(self):
        return str(self.hora)+"-"+str(self.minuto)
