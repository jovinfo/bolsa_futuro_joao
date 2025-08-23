# Exercícios Avançados de Python
# Nível: Intermediário/Avançado

# 1. Crie um programa que leia um arquivo texto chamado 'dados.txt' e conte quantas vezes cada palavra aparece no arquivo. Exiba o resultado em ordem decrescente de frequência.
# Dica: Use o módulo collections.Counter para contar as palavras. Lembre-se de remover pontuação e normalizar para minúsculas antes de contar. Para ordenar, utilize o método most_common().

# 2. Implemente uma função que recebe um dicionário onde as chaves são nomes de alunos e os valores são listas de notas. Retorne um novo dicionário com a média de cada aluno e indique quais alunos estão acima da média geral da turma.

# 3. Escreva um programa que simule um sistema de cadastro de produtos. O usuário pode adicionar, remover e listar produtos (nome, preço e quantidade) usando um menu interativo. Os dados devem ser salvos em um arquivo JSON.
# Dica: Utilize o módulo json para salvar e carregar os dados. Implemente funções separadas para adicionar, remover e listar produtos. Use um loop while para o menu e trate possíveis erros de entrada do usuário.

# 4. Crie uma função recursiva para calcular o fatorial de um número, mas que também imprima cada chamada recursiva feita.
# Dica: Imprima o valor de n a cada chamada da função. Lembre-se de definir o caso base corretamente (n == 0 ou n == 1). Teste sua função com diferentes valores de n para observar o fluxo recursivo.

# 5. Dado um texto, escreva uma função que encontre a palavra mais longa e a mais curta, desconsiderando pontuação.

# 6. Faça um programa que leia uma matriz (lista de listas) de números inteiros e retorne a soma dos elementos da diagonal principal e da diagonal secundária.
# A diagonal principal é formada pelos elementos em que o índice da linha é igual ao índice da coluna (ex: [0][0], [1][1], [2][2], ...).
# A diagonal secundária é formada pelos elementos em que a soma dos índices da linha e da coluna é igual ao tamanho da matriz menos 1 (ex: [0][n-1], [1][n-2], [2][n-3], ...).

# 7. Implemente um jogo simples de adivinhação: o computador escolhe um número aleatório entre 1 e 100, e o usuário deve tentar adivinhar, recebendo dicas se o palpite é maior ou menor que o número secreto. O programa deve contar o número de tentativas.

# 8. Escreva uma função que recebe uma lista de strings e retorna um dicionário agrupando as palavras por quantidade de letras.
# Considere a lista: palavras = ['python', 'java', 'c', 'javascript', 'go', 'ruby', 'swift', 'kotlin', 'perl', 'php']

# 9. Crie um programa que leia uma lista de dicionários representando pessoas (nome, idade, cidade) e permita filtrar por cidade e ordenar por idade.
# Considere a lista:
# pessoas = [
#     {'nome': 'Ana', 'idade': 28, 'cidade': 'São Paulo'},
#     {'nome': 'Bruno', 'idade': 22, 'cidade': 'Rio de Janeiro'},
#     {'nome': 'Carla', 'idade': 35, 'cidade': 'Belo Horizonte'},
#     {'nome': 'Daniel', 'idade': 19, 'cidade': 'São Paulo'},
#     {'nome': 'Eduarda', 'idade': 40, 'cidade': 'Curitiba'}
# ]

# Bons estudos!
