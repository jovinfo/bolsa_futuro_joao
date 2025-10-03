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