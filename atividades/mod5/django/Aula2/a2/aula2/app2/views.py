from .models import Produto, Cliente, Funcionario, Venda # Importa o Model Produto que acabamos de criar
from django.http import HttpResponse

def index(request):
    return HttpResponse("Página funcionando!")

def listar_produtos(request):
    #O ORM irá buscar todos os produtos com a linha abaixo
    todos_produtos = Produto.objects.all()
    
    #Cria um dicionário de contexto para passar os dados para o Template
    lista_de_nomes = [item.nome for item in todos_produtos]
    
    #Renderiza o template 'produtos.html', passando o dicionário de contexto
    return HttpResponse(f"Itens encontrados no DB: {', '.join(lista_de_nomes)}")

def cliente(request):
    #O ORM irá buscar todos os produtos com a linha abaixo
    clientes = Cliente.objects.all()
    
    #Cria um dicionário de contexto para passar os dados para o Template
    lista_de_nomes = [item.nome for item in clientes]
    
    #Renderiza o template 'produtos.html', passando o dicionário de contexto
    return HttpResponse(f"Clientes encontrados no DB: {', '.join(lista_de_nomes)}")

def funcionario(request):
    #O ORM irá buscar todos os produtos com a linha abaixo
    funcionarios = Funcionario.objects.all()
    
    #Cria um dicionário de contexto para passar os dados para o Template
    lista_de_nomes = [item.nome for item in funcionarios]
    
    #Renderiza o template 'produtos.html', passando o dicionário de contexto
    return HttpResponse(f"Funcionarios encontrados no DB: {', '.join(lista_de_nomes)}")

def venda(request):
    #O ORM irá buscar todos os produtos com a linha abaixo
    vendas = Venda.objects.all()
    
    #Cria um dicionário de contexto para passar os dados para o Template
    lista_de_nomes = [item.nome for item in vendas]
    
    #Renderiza o template 'produtos.html', passando o dicionário de contexto
    return HttpResponse(f"Vendas encontrados no DB: {', '.join(lista_de_nomes)}")