from django.contrib import admin
from .models import Produto, Perfil, Venda, ItemVenda


@admin.register(Produto)
class ProdutoAdm(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'qtde', 'data')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('preco', 'qtde')


@admin.register(Perfil)
class PerfilAdm(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'telefone', 'cidade')
    search_fields = ('cliente__username',)


@admin.register(Venda)
class VendaAdm(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data')
    list_filter = ('data',)


@admin.register(ItemVenda)
class ItemVendaAdm(admin.ModelAdmin):
    list_display = ('id', 'venda', 'produto', 'qtde')