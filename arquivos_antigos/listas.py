import random

#Função para uma lista randômica:
def random_list(quant,min,max):
    listinha = []
    for i in range(quant):
        listinha.append(random.randint(min,max))
    return listinha

exemplo = random_list(5,1,15)

print(exemplo)

# #Retorna a posição escolhida da lista pelo índica:
# print(exemplo[2])

# #Adicionando um item:
# exemplo.append(22)
# print(exemplo)

# #Inserindo um item numa posição específica:
# exemplo.insert(0,0)
# print(exemplo)

#Adicionando uma lista ao final de outra
add = [100,100,200,300]
exemplo.extend(add)
print(exemplo)

# #Removendo um item específico da lista:
# exemplo.remove(100)
# print(exemplo)

# #Removendo um item por índice:
# exemplo.pop(1)
# print(exemplo)

# #Removendo um item do final da lista:
# exemplo.pop()
# print(exemplo) 

# #removendo por índice:
# del exemplo[0]
# print(exemplo)

# #Verificando se um item existe na lista:
# print(200 in exemplo)

# #Contando quantas vezes um item aparece na lista:
# print(exemplo.count(100))

# #Ordena a lista (permanentemente)
# exemplo.sort()
# print(exemplo)

# #Retorna a lista ordenada sem modificar a original:
# print(sorted(exemplo))

# #Inverte a lista permanente:
# exemplo.reverse()
# print(exemplo)

# #Tamanho da lista:
# print(len(exemplo))


# #Dicas úteis:
# #Para visualizar uma lista revertida sem mexer nela permanentemente é possível utilizar o seguinte comando:
# print(exemplo[::-1])

# #Para não visualizar itens do final da lista é possível fazer:
# print(exemplo[:-2])