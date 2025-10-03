# 1 - Construa uma classe para armazenar informações de carros, cada objeto instanciado por essa classe deve ter os seguintes atributos:
# A - Modelo, marca, ano de lançamento, potência (1.0,1.6,etc), tipo de câmbio (manual ou automático), preço no lançamento.
# B - Crie um método para retornar cada atributo.
# Crie ao menos 3 instâncias de objeto, e execute todos os métodos para teste.

class Carro:
    def __init__(self,modelo,marca,ano,pot,cambio,preco):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.pot = pot
        self.cambio = cambio
        self.preco = preco

    def get_modelo(self):
        return self.modelo

    def get_marca(self):
        return self.marca

    def get_ano(self):
        return self.ano

    def get_potencia(self):
        return self.pot

    def get_cambio(self):
        return self.cambio

    def get_preco(self):
        return self.preco

car1 = Carro("Ford-T", "Ford", 1964, "1.0", "Manual", 12000)
car2 = Carro("Fordy-A", "Aord", 8888, "1.6", "Automático", 999999)
car3 = Carro("Tord-F", "Tord", 2029, "2.0", "Automático", 250000)

print(car3.get_modelo()) # Tord-F
print(car2.get_marca())  # Aord
print(car1.get_ano())    # 1964
print(car2.get_potencia()) # 1.6
print(car1.get_cambio()) # Manual
print(car3.get_preco()) # 250000