class Fecha:
    def __init__(self,dia,mes,año):
        self.dia = dia
        self.mes = mes
        self.año = año
    
    def get_fecha(self):
        return str(self.dia)+"-"+str(self.mes)+"-"+str(self.año)
