from abc import ABC, abstractmethod
from transporte import Transporte, Caminhao, Navio

class Logistica(ABC):
    @abstractmethod
    def cria_transporte(self) -> Transporte:
        pass

    def planejar_entrega(self):
        transporte = self.cria_transporte()
        transporte.entregar()

class LogisticaTerreste(Logistica):
    def cria_transporte(self) -> Transporte:
        return Caminhao()
    
class LogisticaMaritima(Logistica):
    def cria_transporte(self) -> Transporte:
        return Navio()