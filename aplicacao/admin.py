from django.contrib import admin

from .models import Produto, Perfil, Venda, ItemVenda

admin.site.register(Produto)

@admin.register(Produto)
class ProdutoAdm(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'qtde', 'data')
    list_display_links = ('nome', )
    search_fields = ('nome', )
    list_filter = ('preco', 'qtde')

@admin.register(Perfil)
class PerfilAdm(admin.ModelAdmin):
    list_display = ('id', 'client', 'telefone', 'cidade')
    searchfields = ('cliente__username',)

@admin.register(Venda)
    list_display = ('id', 'cliente', 'data')
    list_filter = ('data',)

@admin.register(ItemVenda)
class ItemVendaAdm(admin.ModelAdmin):
    list_display = ('id', 'venda', 'produto', 'qtde')
    

