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