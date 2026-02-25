from django.urls import path
from .views import index
from .views import contato, produto, cadastrarProduto, salvarProduto

urlpatterns = [

    path('', index),
    path('contato', contato, name="urlcontato"),
    path('produto', produto, name="urlproduto"),
    path('cadastrarProduto', cadastrarProduto, name= 'urlcadastrarProduto')
    path('salvarProduto', salvarProduto, name= 'urlsalvarProduto' )



]