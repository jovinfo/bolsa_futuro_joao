# 1 - Crie uma função chamada "gera_lista". Essa função deve receber como parâmetro um número inteiro com o total de números que a lista deve conter, e retornar a lista gerada. Os números devem ser do tipo inteiro e  gerados aleatoriamente utilizando a biblioteca random.
# Exemplo de chamada: gera_lista(5)
# Exemplo de retorno: [6,25,60,16,5]

import random
from os import system as sys
from pprint import pprint as pp

def gerar_lista(total_numeros:int) -> list[int]:
    lista = []
    for numero in range(0, total_numeros):
        lista.append(random.randint(1,100))
    return lista

# print(gerar_lista(2))

# 2 - Crie uma função chamada "analisar_numeros". Essa função deve receber como parâmetro uma lista contendo 200 números gerados a partir da função do exercício 1 e retornar um dicionário contendo as seguintes informações:
# A - O total de números na lista
# B - A quantidade de números pares
# C - A quantidade de números ímpares
# D - A soma de todos os números
# E - A média dos números
# F - Os números primos presentes na lista.

#TODO fazer o contador caminhar até metade do numero na checagem de primos
#Receber a lista de 200 primos ao inves de checar um por um, evitando checar mesmo numero varias vezes
#Retornar uma lista com 200 booleanos t or f
#Se for repitido botar f nas proximas iterações?
def checar_primo(num:int):
    if num < 2:
        # print('menor q dois')
        return False
    
    primos = [2]
    i = 3

    while True:
        # print(i)
        if num in primos:
            return True
        if num % primos[-1] == 0:
            return False
        # print(primos)

        #Checar se o contador(i) é primo, fazendo a logica:
        #se i for divisivel por qualquer numero da lista primos:
        #não é primo
        #senao, é primo e deve ser adicionado a lista de primos e dar continuidade no loop
        if i not in primos:
            divisivel = False

            for primo in primos:
                if i % primo == 0:
                    divisivel = True
                    # print(f'{i} é divisível por {primo} portanto não é primo')
                    break

            if not divisivel:
                # print('Appendind i to primos')
                primos.append(i)

        # print(primos)

        i += 1

def analisar_numeros(lista_numeros:list[int]) -> dict:
    res = {}
    pares = impares = 0
    primos = []

    total = len(lista_numeros)
    res['total'] = total

    for numero in lista_numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        if checar_primo(numero):
            if numero not in primos:
                primos.append(numero)
        
    res['pares'] = pares
    res['impares'] = impares
    res['soma'] = sum(lista_numeros)
    res['media'] = res['soma'] / total
    res['primos'] = primos

    return res

print(analisar_numeros(gerar_lista(200)))

# 3 - Utilizando o arquivo "contatos.txt", crie uma função chamada "limpa_tel" que deve receber dois parâmetros, arquivo_entrada e arquivo_saida. A função deverá limpar os dados contidos no arquivo e produzir um novo arquivo contendo somente os números de telefone, sem espaços ou caracteres especiais, 1 telefone por linha, com o nome escolhido através do parâmetro "arquivo saída".

def limpa_tel(entrada, saida):
    try:
        with open(entrada, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

    except FileNotFoundError as err:
        return f"tente novamente o arquivo {entrada} não existe nessa pasta \n{err}"
    
    telefones = conteudo.splitlines()
    for telefone in telefones:
        tel_mod = telefone.strip()
        telefones_limpos = []
        for char in tel_mod:
            novo_tel = ''
            digitos = [str(i) for i in range(10)]
            if char in digitos:
                novo_tel += char
            # novo_tel = novo_tel + char
           
            # pp(novo_tel)
        telefones_limpos.append(novo_tel)
    pp(telefones_limpos)
    return f""
sys('cls')

pp(limpa_tel(r'C:\Users\LACE 3\Desktop\aaaa\bolsa_futuro_joao\atividades\mod2\contatos.txt',1))
# pp(limpa_tel('contatos.txt',1))

# 4 - Crie uma classe chamada "Filme". Siga as instruções na sequência:
# A - Os atributos de instância a serem inicializados devem ser: titulo, diretor, ano_lancamento, duracao, nota_imdb. 
# B - A classe deve conter um método chamado detalhes, que retorna uma string contendo o titulo do filme, o nome do diretor, o ano em que foi lançado, sua duracao e sua nota no imdb.
# C - Crie pelo menos 3 instâncias para demonstrar o uso.

# class Filme():


# 5 - Crie uma classe chamada "Termometro". Siga as instruções na sequência.
# A - O atributo de inicialização deve ser: temperatura_celsius.
# B - Crie dois métodos: "aumentar_temp(valor)" e "diminuir_temp(valor)". Os métodos devem ser capazes de alterar a temperatura segundo o valor imputado.
# C - Crie um terceiro método: "temperatura_atual" que deve printar na tela a temperatura naquele momento.
# D - Crie um quarto método: "converte_farenheit" que deve calcular e retornar a temperatura atual convertida para farenheit.
# Para teste utilize os seguintes valores:
# Inicia em 25
# Exibe temperatura
# Aumenta em 25
# Exibe temperatura
# Diminui em 50
# Exibe temperatura
# Converte para Farenheit e exibe na tela.
