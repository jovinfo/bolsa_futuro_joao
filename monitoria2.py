# 1- Crie um programa que exiba a mensagem "Olá, Mundo!" na tela.
if False:
    print("Olá, Mundo!")

    # 2- Crie uma variável para armazenar seu nome e em seguida exiba uma mensagem de boas-vindas que inclua seu nome.
    nome = "João"
    print(f"Bem vindo, {nome}")

    # 3- Crie duas variáveis com números inteiros e exiba a soma delas.
    n1 = 10
    n2 = -5
    print(f"A soma é {n1+n2}")

# 4- Peça ao usuário para digitar seu nome e em seguida exiba uma mensagem de boas-vindas com o nome fornecido.
    nome2 = input("Digite seu nome:")
    print(f"Bem vindo, {nome2}")

# 5- Peça ao usuário para digitar o ano em que nasceu, calcule e exiba sua idade aproximada.
    nascimento = int(input('Digite o ano que você nasceu:'))
    print(f'Sua idade aproximada é de {2025 - nascimento} anos')

# 6- Peça ao usuário para inserir duas notas, calcule a média e exiba o resultado.
    nota1 = float(input("Insira a nota 1:"))
    nota2 = float(input("Insira a nota 2:"))
    print(f"A média das duas notas é {(nota1 + nota2)/2}")

# 7- Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais).
    age = int(input("Qual a sua idade?:"))
    if age >= 18:
        print("Você é maior de idade")
    else: print("Você é menor de idade")

# 8- Peça um número e verifique se ele é positivo, negativo ou zero.
    num = float(input("Digite um número:"))
    if num == 0:
        print("O número é zero")
    elif num > 0:
        print("É um número positivo")
    else: print("É um numero negativo")

# 9- Peça um número e informe se ele é par ou ímpar.
    num2 = int(input("Digite um número:"))
    if num2 % 2 == 0:
        print(f"O número {num2} é par")
    else: print(f"O número {num2} é impar")

# 10- Crie uma senha (ex: "1234") e peça para o usuário digitá-la. Informe se a senha está correta ou incorreta.
    segredo = '121212'
    senha = input("Digite a senha:")
    if segredo == senha:
        print("A senha está correta!")
    else: print("A senha está incorreta :(")

# 11- Peça o valor de uma compra e, se for maior que R$ 100,00, aplique um desconto de 10%. Exiba o valor final.
    compra = float(input("Qual o valor da compra?"))
    if compra > 100:
        compra = compra * .9
    print(f"O valor da sua compra é de {compra}")

# 12- Peça uma letra ao usuário e verifique se é uma vogal ou uma consoante.
    vogais = ['a','e','i','o','u']
    letra = input("Digite uma letra:")
    if letra in vogais:
        print("É uma vogal")
    else: print("É uma consoante")

# 13- Peça dois números e informe qual deles é o maior, ou se são iguais.
    num1 = float(input("Digite um número:"))
    num2 = float(input("Digite outro número:"))
    if num1 > num2:
        print("O primeiro número é maior")
    elif num1 == num2:
        print("Oa números são iguais")
    else: print("O segundo número é maior")

# 14- Crie um programa que exiba os números de 1 a 10.
    for i in range(1,11):
        print(i)

# 15- Peça um número ao usuário e exiba a tabuada de multiplicação desse número, de 1 a 10.
    tabuada = int(input("Escolha um número para fazer a tabuada: "))
    for i in range(1,11):
        print(f"{i} X {tabuada} = {i*tabuada}")

# 16- Peça números ao usuário até que ele digite 0. Ao final, exiba a soma de todos os números digitados.

    soma = num = float(input("Digite um número:"))
    while num != 0:
        num = float(input("Digite um número:"))
        soma += num
    print(f"A soma de todos os números digitados é de: {soma}")

# 17- Crie um programa que peça uma senha ao usuário. Enquanto a senha não for "1234", continue pedindo.
    segredo = "1234"
    senha = input("Qual a senha?:")
    while segredo != senha:
        senha = input("SENHA ERRADA. Qual a senha?:")

# 18- Crie um programa que faça uma contagem regressiva de 10 até 0.
    for i in range(10,-1,-1):
        print(i)

# 19- Crie um número secreto e peça ao usuário para adivinhar. Dê dicas se o palpite foi maior ou menor, até ele acertar.
    num_segredo = 369
    senha = int(input("Qual o número secreto?:"))
    while num_segredo != senha:
        if num_segredo < senha:
            print("Tente um número menor")
        else: print("Tente um número maior")
        senha = int(input("Qual o número secreto?:"))
    print("Parabéns você acertou o número!")

# 20- Crie um programa que itere de 1 a 20 e exiba apenas os números pares.
    for i in range(1,21):
        if i % 2 == 0:
            print(i)

# 21- Peça um número e calcule o seu fatorial (ex: 5! = 5 * 4 * 3 * 2 * 1).
    res = fat = int(input("Escolha um número inteiro para cacular o fatorial:"))

    for i in range(fat - 1,0,-1):
        res *= i
    print(res)

# 22- Crie uma lista com 5 nomes de frutas e exiba cada fruta da lista.
    frutas = ['Banana', 'Maça', 'Pera', 'Uva', 'Jaboticaba']
    for fruta in frutas:
        print(fruta)

# 23- Crie uma lista vazia e peça ao usuário para inserir 5 itens de uma lista de compras. Ao final, exiba a lista completa.
    lista = []
    for i in range(5):
        lista.append(input("Digite um item pra lista:"))
    print(lista)

# 24- Dada uma lista de notas [7, 8, 5, 9, 6], calcule a média e exiba o resultado.
    notas = [7, 8, 5, 9, 6]
    media = sum(notas)/5
    print(f"A média das notas é {media}")

# 25- Dada uma lista de números [10, 23, 4, 7, 15], encontre e exiba o maior e o menor número.
    numeros = [10, 23, 4, 7, 15]
    print(f'O maior número na lista é {max(numeros)}\nO menor número da lista é {min(numeros)}')

# 26- Crie uma lista de nomes e peça um nome ao usuário. Verifique se o nome está na lista e exiba uma mensagem correspondente.
    nomes = ['Joao', 'Rafaella', 'Iara', 'Teresa']
    nome = input("Digite seu nome:")
    if nome in nomes:
        print("O seu nome está na lista")
    else: print("O seu nome não está na lista")

# 27- Crie uma função que exiba a mensagem "Bem-vindo ao programa!" e em seguida chame essa função.
    def welcome():
        print("Bem-vindo ao programa!")
        return
    
    welcome()

# 28- Crie uma função que receba um nome como parâmetro e exiba uma saudação personalizada.
    def saudar(nome:str):
        print(f"Bem vindo {nome}")
        return

    saudar("Nome")
# 29- Crie uma função que receba dois números como parâmetros e retorne a soma deles.
    def somar(n1:float,n2:float):
        return n1 + n2

    print(somar(10,22))

# 30- Crie uma função que receba uma lista de números como parâmetro e retorne a média dos valores.
def media(numeros:list):
    return sum(numeros)/len(numeros)

print(media([7, 8, 5, 9, 6]))