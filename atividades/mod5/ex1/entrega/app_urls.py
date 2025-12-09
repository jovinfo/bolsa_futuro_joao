from django.urls import path
from . import views

urlpatterns = [
    #caminho ficará assim: http://127.0.0.1:8000/loja/home
    path("home/", views.home,name="Home"),
    #caminho ficará assim: http://127.0.0.1:8000/loja/servicos
    path("servicos/", views.servicos,name="Servicos"),
    #caminho ficará assim: http://127.0.0.1:8000/loja/fale_conosco
    path("fale_conosco/", views.fale_conosco,name="FaleConosco"),

]