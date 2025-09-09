# 1 - Utilizando apenas código python, leia o arquivo "nomes.txt" em anexo a este exercício e execute as seguintes tarefas:
# A- Leia o conteúdo e print o resultado na tela.
# B- Verifique o conteúdo de cada linha, como está a formatação? Formate os nomes para que obedeçam ao padrão de escrita, primeira letra de cada nome maiúscula, sem espaços antes ou depois e o que mais for necessário para que tenhamos uma lista de nomes 100% limpos!
# C- Salve o conteúdo limpo num novo arquivo chamado "nomes limpos.txt" com cada nome em uma linha.

# with open("nomes.txt", "r", encoding="utf-8") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)
#     linhas = conteudo.splitlines()
#     nomes_limpos = []
#     for linha in linhas:
#         nova_linha = linha.strip().title()
#         partes = nova_linha.split()
#         nome_limpo = " ".join(partes)
#         nomes_limpos.append(nome_limpo)
#     print(nomes_limpos)

# with open("nomes limpos.txt", "w", encoding="utf-8") as arq_limpo:
#     for linha in nomes_limpos:
#         arq_limpo.write(linha + "\n")



# 2- Utilizando apenas código python, leia o arquivo "vendas.csv" e execute as seguintes tarefas:
# A- Leia o conteúdo do arquivo e print o resultado na tela.
# B- Calcule o valor total em vendas.
# C- Printe o valor total em vendas para o usuário.

#csv : nome, quantidade, preço
# with open('vendas.csv', 'r', encoding='utf-8') as arquivo:
#     conteudo = arquivo.read()
#     linhas = conteudo.splitlines()
#     total = 0
#     for linha in linhas:
#         venda = linha.split(',')
#         total += float(venda[2])
#     print(f"O valor total em vendas é {total:.2f}")


# 3- Construa uma calculadora capaz de realizar as 4 operações matemáticas básicas. Esta calculadora deve obedecer as seguintes regras:
# A- Cada operação matemática deve estar encapsulada em uma função.
# B- Deve existir tratamento de erros/exceções, de forma a prevenir possíveis erros.
# C- Deve conter um menu para execução do programa, onde o usuário só saia do programa quando selecionar a opção de sair.

def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a,b):
    try:
        res = a/b
    except ZeroDivisionError:
        return None
    return res

def multiplicar(a, b):
    return a * b

def receber_numeros():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        return None, None
    
def delay():
    input("Pressione Enter para continuar...")
    print("\n")

while True:
    print('Escolha a operação:\n1 ou "A" para Adição\n2 ou "S" para Subtração\n3 ou "D" para Divisão')
    escolha = input('4 ou "M" para Multiplicação\n5 ou "X" para Sair: ').lower()

    if escolha in ['5', 'x']:
        print("Finalizar")
        break

    elif escolha in ['1', 'a']:
        num1, num2 = receber_numeros()
        if num1 is None:
            print("Entrada inválida. Tente novamente.")
        else:
            print(f"{num1} + {num2} = {adicionar(num1, num2)}")
            delay()
    
    elif escolha in ['2', 's']:
        num1, num2 = receber_numeros()
        if num1 is None:
            print("Entrada inválida. Tente novamente.")
        else:
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
            delay()

    elif escolha in ['3', 'd']:    
        num1, num2 = receber_numeros()
        if num1 is None:
            print("Entrada inválida. Tente novamente.")
        else:
            res = dividir(num1, num2)
            if res is None:
                print("Erro na Divisão. Tente novamente.")
            else:
                print(f"{num1} / {num2} = {res}")
                delay()
    
    elif escolha in ['4', 'm']:
        num1, num2 = receber_numeros()
        if num1 is None:
            print("Entrada inválida. Tente novamente.")
        else:
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            delay()
    
    else:
        print("Opção inválida. Tente novamente.")







