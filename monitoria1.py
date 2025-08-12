
# 1. Crie um programa que solicite ao usuário o preço de três produtos e calcule o valor total da compra.
if False:
    lista_precos = [float(input("Digite o preço de 3 produtos para calcular o total:\nR$ ")),
                    float(input("R$ ")),
                    float(input("R$ "))]
    print(f"O total dos 3 produtos é:R$ {sum(lista_precos)}")


# 2. Desenvolva um programa que peça o ano de nascimento do usuário e o ano atual, e então calcule e exiba a idade do usuário.

    nascimento = int(input("Qual o ano do seu nascimento?"))
    hoje = int(input("Em que ano estamos?"))
    print(f"A sua \"idade\" (dif de anos) é de: {hoje - nascimento} anos")

# 3. Escreva um programa que peça uma palavra ao usuário e um número inteiro, e então imprima a palavra repetida o número de vezes informado.

    palavra = input("Digite uma palavra para repetir: ")
    numero = int(input("Escolha quantas vezes irá repetir: "))
    for i in range(numero):
        print(palavra)

# 4. Crie um programa que solicite o valor total de uma conta de restaurante e o número de pessoas para dividir a conta. Calcule e exiba o valor que cada pessoa deve pagar.

    total = float(input("Qual o valor total da conta? R$ "))
    num_pessoas = int(input("Quantas pessoas vão dividir a conta?"))
    print(f"O valor que cada pessoa deve pagar é de: R$ {total/num_pessoas}")

# 5. Desenvolva um programa que peça ao usuário para inserir as notas de três provas e calcule a média aritmética dessas notas.

    lista_notas = [float(input("Insira as notas das 3 provas para calcular a média aritmética:\n  Prova 1 - ")),
                float(input("Prova 2 - ")),
                float(input("Prova 3 - "))]
    print(f"A média aritmética das três provas é de: {sum(lista_notas)/3}")

# 6. Escreva um programa que peça o peso (em kg) e a altura (em metros) de uma pessoa e calcule o seu Índice de Massa Corporal (IMC), usando a fórmula: IMC = peso / (altura ** 2).

    peso = float(input("Qual seu peso em KG? "))
    altura = float(input("Qual sua altura em Metros "))
    print(f"O seu Índice de Massa Corporal (IMC) é de: {peso / altura ** 2}")

# 7. Crie um programa que receba um número total de segundos e o converta para horas, minutos e segundos, exibindo o resultado.

    dias = int(input("Digite o númedo de dias:"))
    horas = int(input("Digite o númedo de horas:"))
    minutos = int(input("Digite o númedo de minutos:"))
    segundos = int(input("Digite o númedo de segundos:"))

    horas = horas + (dias * 24)
    minutos = minutos + (horas * 60)
    segundos = segundos + (minutos * 60)

    print(f"O total de segundos é {segundos}")

# 8. Crie um programa que solicite o preço de um produto e um percentual de desconto. Calcule e exiba o novo preço do produto após aplicar o desconto.

produto = float(input("Qual o preço do produto?:R$ "))
desconto = float(input("Qual o percentual de desconto?: "))
print(f"O preço desse produto com {desconto}% de desconto é de R$ {produto * (100 - desconto) / 100}")
# produto --- 100
# total ---- 100-desconto
# produto * (100 - desconto) = 100 * total
# total = produto * (100 - desconto) / 100

# 9. Escreva um programa que o usuário defina a quantidade de dias, horas, minutos e segundos em variáveis. Calcule e exiba o total de segundos resultantes da soma de todas as variáveis.

l = []
for i in ['dias', 'horas', 'minutos', 'segundos']:
    l.append(int(input(f"Insira a quantidades de {i}: ")))
# total = (((((l[0] * 24) + l[1] ) * 60) + l[2] ) *60) + l[3]
print(f"O total de segundos é {(((((l[0] * 24) + l[1] ) * 60) + l[2] ) *60) + l[3]}")
