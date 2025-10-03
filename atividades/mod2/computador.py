# Crie 4 classes: Computador, Memoria, Placa_mae, SSD.
# Ao iniciar um computador faz sentido que todos os seus componentes iniciem juntos.
# Se algum deles não for iniciado encontraremos erros, da mesma forma que não faz sentido
# iniciar esses componentes de forma isolada.
# Produza um classe Computador composta pelas classes Memoria, Placa_mae e SSD.

class Computador:
    def __init__(self,cap_ram,modelo_placa,cap_ssd):
        self.memoria = Memoria(cap_ram)
        self.placa_mae = Placa_Mae(modelo_placa)
        self.ssd = SSD(cap_ssd)

class Memoria:
    def __init__(self,capacidade):
        self.capacidade = capacidade

class Placa_Mae:
    def __init__(self,modelo):
        self.modelo = modelo

class SSD:
    def __init__(self,capacidade):
        self.capacidade = capacidade