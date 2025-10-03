# Informações para realização da avaliação:

# Além das regras estipuladas em cada questão, também são avaliados outros quesitos como: clareza e organização do código, e adesão as boas práticas da linguagem.
# Caso não consiga completar uma questão, entregue o código até onde você conseguiu chegar!
# Cada questão deve ser entregue em um arquivo .py separado, cada arquivo com o nome referente a questão: "1.py","2.py","3.py".

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

# 2 - Suponha que estamos desenvolvendo um sistema para um banco. Este sistema deve obedecer as seguintes restrições:
# A - Uma classe pai chamada Cliente, com os atributos: nome, cpf, endereço.
# B - Uma classe filha chamada Conta_Corrente que deve herdar os atributos da classe pai mais o atributo "saldo". Este atributo deve ser privado.
# C - O sistema precisa ser capaz de: depositar, sacar, consultar saldo, consultar informações dos clientes e alterar informações dos clientes. Não deve ser possível ter saldo negativo, nem sacar além do saldo.
# Crie ao menos 1 instância de Conta_Corrente, execute todos os métodos para teste.

class Cliente:
    def __init__(self,nome,cpf,endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
    
class Conta_Corrente(Cliente):
    def __init__(self,nome,cpf,endereco,saldo):
        super().__init__(nome,cpf,endereco)
        self._saldo = saldo

    def consultar_saldo(self):
        return self._saldo
    
    def consultar_infos(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nEndereço: {self.endereco}")

    def alterar_infos(self,nome=None,cpf=None,endereco=None):
        if nome is not None:
            self.nome = nome
        if cpf is not None:
            self.cpf = cpf
        if endereco is not None:
            self.endereco = endereco
        print("Informações atualizadas:")
        self.consultar_infos()

    def checar_valor(self,valor):
        try:
            v = float(valor)
        except ValueError:
            return None
        
        if v <= 0:
            return None
        
        return v
    
    def depositar(self,valor):
        v = self.checar_valor(valor)
        if v is None:
            return None

        self._saldo += v
        return self.consultar_saldo()
    
    def sacar(self,valor):
        v = self.checar_valor(valor)
        if v is None:
            return None

        if v > self._saldo:
            return None
        
        self._saldo -= v
        return self.consultar_saldo()

correntista1 = Conta_Corrente("João", "123.456.789-10", "Casa", 1000)
print(correntista1.consultar_saldo()) # 1000
print(correntista1.depositar(500)) # 1500
# print(correntista1.depositar(-100)) # None
# print(correntista1.depositar("abc")) # None

print(correntista1.sacar(200)) # 1300
print(correntista1.sacar(2000)) # None
# print(correntista1.sacar(-100)) # None
# print(correntista1.sacar("abc")) # None

print(correntista1.consultar_saldo()) # 1300

correntista1.consultar_infos()
correntista1.alterar_infos("Maria","987.654.321-00","Apartamento")



# 3 - Suponha que você faz parte de uma equipe de desenvolvimento para softwares de astronomia e irá criar um protótipo expansível de sistema solar, para isso siga as definições:
# A - Crie uma classe Planeta, ela deve ser inicializada com os parâmetros: nome, raio_equatorial, distancia_do_sol e composicao.

# B - O raio_equatorial deve ser em km, a distancia_do_sol em milhões de km e composição "Rochoso" ou "Gasoso".

# C - Adicione um método de apresentação, sem parâmetros, que mostre na tela as informações do planeta.

# D - Fora da classe, crie uma função que calcule e retorne o valor da distância do planeta instanciado até o SOL em UA (Unidades Astronômicas, representada pela distância da terra até o Sol, aproximadamente 150 milhões de km). Utilize a fórmula: distancia_do_sol / 150. Essa função deve receber como parâmetro o atributo distancia_do_sol da classe planeta, ou seja, deve funcionar para qualquer objeto do tipo planeta.
# Pesquisa na internet pelas informações de 3 planetas e as utilize para instanciar 3 objetos. Execute o método de apresentação e a função de distância para cada um dos objetos instanciados.

def calcular_distancia_ua(distancia_do_sol):
    return distancia_do_sol / 150

class Planeta:
    def __init__(self,nome,raio_equatorial,distancia_do_sol,composicao):
        self.nome = nome
        self.raio_equatorial = raio_equatorial # KM
        self.distancia_do_sol = distancia_do_sol # Milhões de KM
        self.composicao = composicao # "Rochoso" ou "Gasoso"
    
    def apresentar(self):
        print(f"Planeta: {self.nome}\nRaio Equatorial: {self.raio_equatorial} km")
        print(f"Distância do Sol: {self.distancia_do_sol} milhões de km\nComposição: {self.composicao}")

planeta1 = Planeta("Marte", 3389.5, 228, "Rochoso")
planeta2 = Planeta("Júpiter", 69911, 778, "Gasoso")
planeta3 = Planeta("Terra", 6371, 149.6, "Rochoso")

planeta1.apresentar()
print(f"Distância do Sol em UA: {calcular_distancia_ua(planeta1.distancia_do_sol):.2f}\n")

planeta2.apresentar()
print(f"Distância do Sol em UA: {calcular_distancia_ua(planeta2.distancia_do_sol):.2f}\n")

planeta3.apresentar()
print(f"Distância do Sol em UA: {calcular_distancia_ua(planeta3.distancia_do_sol):.2f}\n")