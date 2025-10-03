class Capitulo:
    def __init__(self,texto):
        self.texto = texto

class Livro:
    def __init__(self,autor):
        self.autor = autor
        self.capitulos = []

    def adicionar_capitulo(self, capitulo: Capitulo):
        self.capitulos.append(capitulo.texto)

livro = Livro('Machadão')
cap1 = Capitulo("Era uma vez um capitulo")
cap2 = Capitulo("Era uma vez um capitulo2")
livro.adicionar_capitulo(cap1)
livro.adicionar_capitulo(cap2)
print(livro.capitulos)
