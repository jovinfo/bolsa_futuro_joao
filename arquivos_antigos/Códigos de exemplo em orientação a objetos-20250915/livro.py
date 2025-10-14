# Crie uma classe livro com atributo autor
class Livro:
    def __init__(self,autor, custo):
        self.data_criacao = '06/10/2025'
        self.autor = autor
        self._custo = custo
        self._lucro = custo + 50
    
    def get_autor(self):
        return self.autor
    
    def get_custo(self):
        return self._custo

livro = Livro('Qualqquer coisa',100) #Instancia

# print(livro.get_custo())
print(livro.get_autor())

# print(livro.a)

# def 

# Crie uma classe capitulo com o atributo texto

# Metodo adicionar_capitulo e exibir_capitulos