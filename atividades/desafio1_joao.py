# 1- Crie um programa que deve funcionar como um conversor de temperaturas. Ele deve conter um menu que permita ao usuário selecionar 2 opções:
# Celsius para Fahrenheit
# Fahrenheit para Celsius
# Com base na escolha do usuário, seu programa deve perguntar a ele a temperatura que deseja converter, calcular, e mostrar o resultado na tela para o usuário.
# Fórmulas: 
# Fahrenheit = (Celsius * 9/5) + 32
# Celsius = (Fahrenheit - 32) * 5/9

print('EX1: Conversor de temperaturas')

while True:
    print('Escolha a sua opção:')
    escolha = input('Digite 1 para converter de Fahrenheit para Celsius\nDigite 2 para converter de Celsius para Fahrenheit: ')
    if escolha == '1':
        temp_f = float(input('Insira a sua temperatura em Fahrenheit: '))
        temp_c = (temp_f - 32) * 5/9
        print(f'A temperatura convertida é de {temp_c} °C')
        break
    elif escolha == '2':
        temp_c = float(input('Insira a sua temperatura em Celsius: '))
        temp_f = (temp_c * 9/5) + 32
        print(f'A temperatura convertida é de {temp_f} °F')
        break
    else:
        print('Escolha inválida, tente novamente:')
    
# 2- Dada a seguinte lista:
# temperaturas = [28.5, 29.1, 27.3, 25.4, 23.9, 22.7, 22.1, 23.5, 24.6, 26.8, 27.9, 28.8]
# Crie um programa que:
# A- Mostre a menor temperatura registrada:
# B- Mostre a maior temperatura registrada:
# C- Mostre a média de temperatura.
# Para este desafio é proibido o uso das funções built-in do python: max(),min() e sum().

temperaturas = [28.5, 29.1, 27.3, 25.4, 23.9, 22.7, 22.1, 23.5, 24.6, 26.8, 27.9, 28.8]
soma = 0
menor = maior = temperaturas[0]
for temperatura in temperaturas:
    soma += temperatura
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
media = soma/len(temperaturas)
print('\nEX2: Comparação de temperaturas')
print(f'A menor temperatura é de: {menor}')
print(f'A maior temperatura é de: {maior}')
print(f'A média das temperaturas da lista é de: {media}')

# 3- Você deve criar um programa para controle de estoque de uma loja de decoração, seu programa deve permitir que o usuário realize as seguintes operações:
# A- Criar o estoque: (Deve ser obrigatoriamente um dicionário)
# B- Adicionar itens utilizando o nome do item e a quantidade.
# C- Consultar um item, utilizando o nome do produto.
# D- Atualizar a quantidade em estoque de um item.
# E- Exibir o estoque final.
# F- Sair do programa.
# O usuário deve continuar vendo o menu e podendo fazer operações até que selecione uma opção de saída do programa.

opcoes = """A - Criar o estoque
B - Adicionar itens utilizando o nome do item e a quantidade.
C - Consultar um item, utilizando o nome do produto.
D - Atualizar a quantidade em estoque de um item.
E - Exibir o estoque final.
F - Sair do programa.
"""

def listar_produtos():
    print('Os produtos que temos cadastrados são:')
    for produto in estoque.keys():
        print(produto)

criado = False
print('\n\nEX3: Controle de estoque')
while True:
    escolha = input(f"\nEscolha a sua opção de \'A\' - \'F\'\n{opcoes}\n").lower()
    if escolha in ['a','b','c','d','e','f']:
        if escolha == 'a':
            if criado:
                print('O estoque já existe!')
            else:
                estoque = {}
                criado = True
                print('O estoque foi criado!')
        
        elif escolha == 'b':
            if not criado:
                print("Primeiro você deve escolher a opção 'A' para criar o estoque")
            else:
                prod_nome = input("Insira o nome do produto a ser criado: ").lower()
                while prod_nome in estoque.keys():
                    prod_nome = input(f"Esse nome de produto '{prod_nome}' já existe" \
                                    "\nInsira o nome de um #NOVO# produto para ser criado: ").lower()
                prod_quant = float(input(f"Insira a quantidade de {prod_nome} que tem no estoque: "))
                estoque[prod_nome] = prod_quant
                print(f'O produto {prod_nome} foi criado com a quantidade {prod_quant}')
            
        elif escolha == 'c':
            if not criado:
                print("Primeiro você deve escolher a opção 'A' para criar o estoque")
            else:
                if len(estoque) > 0:
                    listar_produtos()
                    consulta = input('Digite o nome do produto que deseja consultar: ').lower()
                    while consulta not in estoque.keys():
                        listar_produtos()
                        consulta = input(f"Esse nome de produto '{consulta}' não existe!" \
                                    "\nDigite o nome do produto que deseja consultar: ").lower()
                    print(f'O produto \'{consulta}\' tem {estoque[consulta]} no estoque.')
                else:
                    print("Primeiro você deve escolher a opção 'B' para criar um produto no estoque")

        elif escolha == 'd':
            if not criado:
                print("Primeiro você deve escolher a opção 'A' para criar o estoque")
            else:
                if len(estoque) > 0:
                    listar_produtos()
                    alterar = input('Digite o nome do produto que deseja alterar a quantidade: ').lower()
                    while alterar not in estoque.keys():
                        listar_produtos()
                        alterar = input(f"Esse nome de produto '{alterar}' não existe!" \
                                    "\nDigite o nome do produto que deseja alterar: ").lower()
                    print(f'O produto \'{alterar}\' tem {estoque[alterar]} no estoque.')
                    nova_qtd = float(input(f'Qual seria a nova quantidade do produto \'{alterar}\'? '))
                    estoque[alterar] = nova_qtd
                    print(f'O produto \'{alterar}\' foi atualizado e agora tem {estoque[alterar]} no estoque.')
                else:
                    print("Primeiro você deve escolher a opção 'B' para criar um produto no estoque")

        elif escolha == 'e':
            if not criado:
                print("Primeiro você deve escolher a opção 'A' para criar o estoque")
            else:
                if len(estoque) > 0:
                    print(f'O seu estoque final é de:')
                    for prod, qtd in estoque.items():
                        print(f'O produto \'{prod}\' tem {qtd} no estoque')
                else:
                    print("Primeiro você deve escolher a opção 'B' para criar um produto no estoque")

        elif escolha == 'f':
            print('Você escolheu sair, o programa será finalizado!')
            break
    
    else:
        print(f'Opção \'{escolha}\' inválida')


# 4- Crie uma função baseada na premissa do exercício número 1, os parâmetros a serem recebidos devem ser:
# A - Unidade de medida destino da conversão.
# B - Valor a ser convertido.
# O retorno da função deve ser o valor calculado na conversão.
print('\nEX4: Função conversor de temperaturas')
def converter_temp(unidade_final, valor):
    if unidade_final == 'c':
        res = (valor - 32) * 5/9
        return res
    elif unidade_final == 'f':
        res = (valor * 9/5) + 32
        return res
    else:
        return None

while True:
    print('Conversor de temperaturas! Escolha a unidade de medida destino da conversão')
    print('Digite \'C\' para converter para Celsius')
    final = input('Digite \'F\' para converter para Fahrenheit: ').lower()
    temp_inicial = float(input('Insira a sua temperatura a converter: '))
    res = converter_temp(final, temp_inicial)
    if res is None:
        print('Escolha uma opção válida!')
    else:
        print(f'O resultado da conversão é de {res:.2f} °{final.upper()}')
        break