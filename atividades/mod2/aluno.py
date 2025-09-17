class Aluno():
    def __init__(self,codigo,nome,idade,altura_m,telefone):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.altura_m = altura_m
        self.telefone = telefone
    
    def retorna_atributos(self):
        return f'{self.codigo=}\n{self.nome=}\n{self.idade=}\n{self.altura_m=}\n{self.telefone=}'
    
    def editar_aluno(self, nome,idade,altura_m,telefone):
        self.nome = nome
        self.idade = idade
        self.altura_m = altura_m
        self.telefone = telefone
    
aluno = Aluno(1,'Joao', 24, 1.70, '999999999')
print(aluno.retorna_atributos())
aluno.editar_aluno('Oajo', 22, 1.33, '1213123123')
print(aluno.retorna_atributos())