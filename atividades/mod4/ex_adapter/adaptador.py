from parser import LeitorDeMov, LeitorDeAvi

class LeitorDeArquivosAdapter:
    def __init__(self, tipo_caminho):
        self.tipo = tipo_caminho[0]
        self.caminho = tipo_caminho[1]
    
    def converter(self):
        if self.tipo == 'mov':
            return LeitorDeMov.converter(self.caminho)
        elif self.tipo == 'avi':
            return LeitorDeAvi.converter(self.caminho)
        
