from django.db import models

#Create your models here

class Produto(models.Model): #Lembre-se que essa herança é fundamental!
    """
    Esta classe irá criar uma tabela Produto no banco de dados com os campos
    nome
    preco
    disponivel
    """
    cod = models.IntegerField()
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    #Método de representação preferido para facilitar a visualização no shell e admin
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    cod = models.IntegerField()
    nome = models.CharField(max_length=33)
    cpf = models.CharField(max_length=11)
    
class Funcionario(models.Model):
    cod = models.IntegerField()
    nome = models.CharField(max_length=33)
    cpf = models.CharField(max_length=11)
    salario = models.DecimalField(max_digits=11, decimal_places=2)
    
class Venda(models.Model):
    cod_prod = models.IntegerField()
    cod_func = models.IntegerField()
    cod_cliente = models.IntegerField()
    total = models.DecimalField(max_digits=7, decimal_places=2)
    
#Lembre-se:

#Depois de modificar este arquivo você precisa executar os dois comandos de terminal que aplicam alterações.

#python manage.py makemigrations nome_do_app

#python manage.py migrate