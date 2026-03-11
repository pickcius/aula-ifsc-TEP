from django.urls import path
from .views import index, contato, produto, entrar, sair 
from .views import cadastrarProduto, salvarProduto, editarProduto, excluirProduto
from .views import cadastrarUsuario

urlpatterns = [
    path('', index, name="urlindex"),
    path('contato', contato, name="urlcontato"),
    path('produto', produto, name="urlproduto"),
    path('cadastrarProduto', cadastrarProduto, name="urlcadastrarProduto"),
    path('salvarProduto', salvarProduto, name="urlsalvarProduto"),
    path('editarProduto/<int:id>', editarProduto, name="urleditarProduto"),
    path('excluirProduto/<int:id>', excluirProduto, name="urlexcluirProduto"),
    path('entrar', entrar, name="urlentrar"),
    path('sair', sair, name="urlsair"),
    path('cadastrarUsuario', cadastrarUsuario, name="urlcadastrarUsuario"),
]