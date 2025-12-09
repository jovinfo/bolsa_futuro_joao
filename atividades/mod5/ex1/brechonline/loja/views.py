from django.http import HttpResponse

#A função a seguir irá lidar com a requisição para o index.
def home(request):
    return HttpResponse("Frente da Loja Brechó Online, Seja bem vindo!")

def servicos(request):
    return HttpResponse("Aqui estão os serviços da Loja Brechó Online. Compre, venda e troque suas roupas usadas!")

def fale_conosco(request):
    return HttpResponse("Fale conosco através do contato (21)99988-7766 ou email: contato@brechonline.com.br")

#Para que essa view seja acessível, o arquivo urls do PROJETO precisa ter o include
#Ele aponta para a URL do APP
#E a URL do APP aponta para View que irá lidar com a requisição!
