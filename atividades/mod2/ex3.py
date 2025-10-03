# 1 - No contexto de modelagem de jogos, crie uma classe Player. Ela deve obedecer as seguintes condições.
# A - Os parâmetros de inicialização do objeto devem ser: nome, vida, mana.
# B - Os atributos vida e mana precisam ser privados.
# C - A classe deve conter métodos que retornem os atributos privados.
# D - A classe deve ter dois métodos públicos: sofrer_dano e usar_magia. Sofrer dano causará dano a vida do player, usar magia diminuirá a mana. É preciso garantir que ambos os atributos não sejam menores do que 0.
# E - A classe deve ter um atributo público chamado "morto", se a vida chegar a 0, esse atributo deve ser modificado para verdadeiro.

from time import sleep

class Player:
    def __init__(self,nome,vida,mana):
        self.nome = nome
        self._vida = vida
        self._mana = mana
        self.morto = False
    
    def get_vida(self):
        return self._vida
    
    def get_mana(self):
        return self._mana
    
    def sofrer_dano(self, dano):
        if self.morto:
            return "Você está morto, não tem como sofrer mais dano"
        if self.get_vida() - dano <= 0:
            self._vida = 0
            self.morto = True
            return f'Você levou {dano} de dano e morreu'
        self._vida =- dano
        return f'Você levou {dano} de dano e está com {self.get_vida}'
    
    def usar_magia(self,custo):
        if self.get_mana() - custo < 0:
            return f'Você não tem a mana para lançar essa magia'
        self._mana -= custo
        return f'Você usou magia'


# 2 - Utilizando a classe Player produzida no exercício 1, faça o seguinte:
# A - Crie 3 classes filhas: Mago, Guerreiro, Arqueiro.
# B - Cada subclasse deve utilizar o inicializador da classe mãe (super().__init__) e adicionar mais 1 atributo específico a cada subclasse, sendo eles: 
# Mago -> elemento.
# Guerreiro -> constituicao.
# Arqueiro -> alcance_de_visao.

# C - As subclasses Mago e Guerreiro devem ter 2 métodos polimórficos:
# A classe Mago terá um método usar_magia (atenção ao conceito de polimorfismo) que gastará sempre 15% a menos de mana.

# A classe Guerreiro deverá ter um método sofrer_dano, onde o atributo "constituicao" será o valor em % de redução de dano que o guerreiro receberia. Exemplo: se constituicao = 25, o guerreiro deve receber menos 25% de dano na vida.

# D- A classe Arqueiro deve ter 2 métodos: disparar_flechas e recarregar_aljava. Ao disparar flechas o arqueiro deve gastar 1% de sua mana por flecha, o máximo de disparos consecutivos deve ser 10. Ao ficar sem flechas ele deve recarregar a aljava, durante este tempo ele deve ficar proibido de disparar por 5 segundos. 

# E - A classe Mago deve ter um método chamado magia_elemental, ele deve consumir 50% da mana atual do mago, e 10% da vida atual.

# F - A classe Guerreiro deve ter um método chamado furia, onde ela consome 10% da vida atual do guerreiro (deve desconsiderar a redução de dano do guerreiro, ou seja, deve ser aplicada direto na vida).

# Sinta-se a vontade para criar atributos nas classes que possam te ajudar a implementar a solução.

class Mago(Player):
    def __init__(self, nome, vida, mana, elemento):
        super().__init__(nome, vida, mana)
        self.elemento = elemento

    def usar_magia(self,custo):
        custo *= 0.85
        if self.get_mana() - custo < 0:
            return f'Você não tem a mana para lançar essa magia'
        self._mana -= custo
        return f'Você usou magia'
    
    def magia_elemental(self):
        self._mana -= self._mana/2
        self._vida -= self._vida/10

class Guerreiro(Player):
    def __init__(self, nome, vida, mana, constituicao):
        super().__init__(nome, vida, mana)
        self.constituicao = constituicao #de 0 a 100

    def sofrer_dano(self, dano):
        dano = dano * (100 - self.constituicao)/100
        if self.morto:
            return "Você está morto, não tem como sofrer mais dano"
        if self.get_vida() - dano <= 0:
            self._vida = 0
            self.morto = True
            return f'Você levou {dano} de dano e morreu'
        self._vida -= dano
        return f'Você levou {dano} de dano e está com {self.get_vida()} de vida'
    
    def furia(self): #10% da vida atual do guerreiro
        self._vida -= self._vida/10

class Arqueiro(Player):
    def __init__(self, nome, vida, mana, alcance_de_visao):
        super().__init__(nome, vida, mana)
        self.alcance_de_visao = alcance_de_visao
        self.flechas = 10

    def disparar_flechas(self):
        if self.flechas < 1:
            return f'Você precisa recarregar antes de disparar novamente'
        self.flechas -= 1
        self._mana -= self._mana/100
        return f'Atirou a flecha, sobraram {self.flechas}'


    def recarregar_aljava(self):
        print('Recarregando, aguarde 5 segundos:')
        for i in range(5,0,-1):
            print(f'{i}')
            sleep(1)
        self.flechas = 10
        print('Recarregado!')

arq = Arqueiro('a',100,50,200)
mago = Mago('m',50,150,'fogo')
gue = Guerreiro('g',200,50,10)
            

# 3 - Crie 3 classes independentes: Circulo, Quadrado, Triangulo. Cada classe deve ter um método desenhar, esse método deve conter um print remetendo ao desenho da forma de sua respectiva classe, exemplo: o método desenhar da classe Circulo deve ter um print parecido com: "desenhando circulo".
# Na sequência crie uma função chamada renderizar_imagem, que deve receber como parâmetro uma lista de objetos das classes de formas, iterar sobre a lista e chamar o método desenhar de cada objeto contido na lista.

# Para teste dessa função: crie uma lista contendo uma instância de Circulo, uma de Quadrado e outra de Triangulo. Passe essa lista como parâmetro na chamada da função renderizar_imagem.

def renderizar_imagem(formas:list):
    for forma in formas:
        forma.desenhar()
    

class Circulo:
    def __init__(self):
        pass
    
    def desenhar(self):
        print("Desenhando o Círculo")

class Quadrado:
    def __init__(self):
        pass
    
    def desenhar(self):
        print("Desenhando o Quadrado")

class Triangulo:
    def __init__(self):
        pass
    
    def desenhar(self):
        print("Desenhando o Triângulo")

l = [Circulo(),Quadrado(),Triangulo()]
renderizar_imagem(l)