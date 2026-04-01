from django.contrib import admin

from .models import Produto, Perfil, Venda, ItemVenda

@admin.register(Produto)
class ProdutoAdm(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'qtde', 'data')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('preco', 'qtde')
    list_editable = ('preco', 'qtde')

@admin.register(Perfil)
class PerfilAdm(admin.ModelAdmin):
    list_display = ('id', 'telefone', 'rua', 'numero', 'cidade')

@admin.register(Venda)
class VendaAdm(admin.ModelAdmin):
    list_display = ('id', 'data')

@admin.register(ItemVenda)
class ItemVendaAdm(admin.ModelAdmin):
    list_display = ('id', 'qtde')