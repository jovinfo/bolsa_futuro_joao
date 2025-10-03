class Capitulo:
    def __init__(self,texto):
        self.texto = texto

class Livro:
    def __init__(self,autor):
        self.autor = autor
        self.capitulos = []

    def adicionar_capitulo(self, capitulo: Capitulo):
        self.capitulos.append(capitulo.texto)
    
    def exibir_capitulos(self):
        for cap in self.capitulos:
            print(f'{cap}\n')

livro = Livro('Machadão')
cap1 = Capitulo("Era uma vez um capitulo")
cap2 = Capitulo("Era uma vez um capitulo2")
cap3  = Capitulo("Era uma vez um capitulo3")
livro.adicionar_capitulo(cap1)
livro.adicionar_capitulo(cap2)
livro.adicionar_capitulo(cap3)
livro.exibir_capitulos()


