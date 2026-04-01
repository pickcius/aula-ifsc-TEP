from django.urls import path
from .views import index, contato, produto, entrar, sair 
from .views import cadastrarProduto, salvarProduto, editarProduto, excluirProduto
from .views import cadastrarUsuario
from .views import carrinho, addcarrinho, delcarrinho
from django.conf.urls.static import static
from django.conf import settings
from . import views

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
    path('carrinho', carrinho, name="urlcarrinho"),
    path('carrinho/<int:id>', addcarrinho, name="urladdcarrinho"),
    path('delcarrinho/<int:id>', delcarrinho, name="urldelcarrinho"),
    path('finalizarCompra', carrinho, name="urlfinalizarCompra"),

    ### CARRINHO
    path('vercarrinho', views.vercarrinho, name="urlvercarrinho"),
    path('vercarrinho/atualizar/<int:item_id>/', views.atualizarcarrinho, name="urlatualizarcarrinho"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)