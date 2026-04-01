from django.conf import settings
from .models import Produto
from decimal import Decimal

class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get(settings.CARRINHO_SESSION_ID, {})
        if not carrinho:
            carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}
        self.carrinho = carrinho
    
    def adicionar(self, produto, qtde=1, atualizar_qtde=False):
        produto_id = str(produto.id)
        if produto_id not in self.carrinho:
            self.carrinho[produto.id] = {'qtde': 0, 'preco': str(produto.preco)}

        if atualizar_qtde:
            self.carrinho[produto_id]['qtde'] = qtde
        else:
            self.carrinho[produto_id]['qtde'] += qtde

        self.salvar()

    def salvar(self):
        self.session[settings.CARRINHO_SESSION_ID] = self.carrinho
        self.session.modified = True

    def remover(self, produto):
        produto_id = str(produto.id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.salvar()

    def __iter__(self):
        produto_ids = self.carrinho.keys()
        produtos = Produto.objects.filter(id__in=produto_ids)
        carrinho = self.carrinho.copy()
    
        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto
            carrinho[str(produto.id)]['preco_total'] = carrinho[str(produto.id)]['qtde'] * produto.preco
            yield carrinho[str(produto.id)]

    def __len__(self):
        return sum(item['qtde'] for item in self.carrinho.values())

    def limpar(self):
        del self.session[settings.CARRINHO_SESSION_ID]
        self.session.modified = True

    def get_total(self):
        return sum(Decimal(item['preco']) * item['qtde'] for item in self.carrinho.values())