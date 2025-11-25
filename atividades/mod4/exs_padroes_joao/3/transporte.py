from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

class Caminhao(Transporte):
    def entregar(self):
        print("Abastecendo o caminhão...")
        print("Carregando a carga no caminhão...")
        print("Caminhão a caminho...")
        print("Entrega realizada por caminhão.")
    
class Navio(Transporte):
    def entregar(self):
        print("Preparando o navio para a viagem...")
        print("Carregando a carga no navio...")
        print("Navio a caminho...")
        print("Entrega realizada por navio.")
