class Carro():
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def acelerar(self):
        return "VROMMMMMM"
    
    def freiar(self):
        return "SCRIIICHHH"
    
    def pintar(self, nova_cor):
        self.cor = nova_cor
        return f'Nova cor do carro é: {self.cor}'
    
    def bater(self):
        return 'Kabum'
    
    def trocar_rodas(self):
        return "Rodas novas!"
