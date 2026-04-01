from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produto, Venda, ItemVenda, Perfil
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UsuarioForm
from .carrinho import Carrinho


### CARRINHO #######
def get_or_create_carrinho(request):
    venda, created = Venda.objects.get_or_create(
        cliente = request.user,
        status = 'P' # Venda Pendente
    )
    return venda

def vercarrinho(request):
    venda = get_or_create_carrinho(request)
    itens = venda.itemvenda_set.all()
    perfil = getattr(request.user, 'perfil', None)

    context = {
        'venda': venda,
        'itens': itens,
        'perfil': perfil
    }

    return render(request, 'vercarrinho.html', context)

def atualizarcarrinho(request, item_id):
    item = get_object_or_404(ItemVenda, id=item_id, venda__cliente=request.user)

    if request.method == 'POST':
        acao = request.POST.get('acao')
        if acao == 'aumentar':
            if item.qtde < item.produto.qtde:
                item.qtde += 1
                item.save()
        elif acao == 'diminuir':
            if item.qtde > 1:
                item.qtde -= 1
                item.save()
            else: # se for 1 e diminuir, então remove
                item.delete()
        elif acao == 'remover':
            item.delete()
    return redirect('urlvercarrinho')


def index(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def contato(request):
    context = {'curso': 'Desenvolvimento de Sistemas'}
    return render(request, 'contato.html', context)

@login_required(login_url="urlentrar")
def produto(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "produto.html", context)

def cadastrarProduto(request):
    return render(request, "cadastrarProduto.html")

def salvarProduto(request):
    thisnome = request.POST.get('txtNome')
    thispreco = request.POST.get('txtPreco')
    thisqtde = request.POST.get('txtQtde')
    thisdata = request.POST.get('txtData')
    thisdescricao = request.POST.get('txtDescricao')
    thisimagem = request.FILES.get('imagem')

    produto = Produto(
        nome = thisnome,
        preco = float(thispreco),
        qtde = thisqtde,
        data = thisdata,
        descricao = thisdescricao,
        imagem = thisimagem
    )

    produto.save()
    return redirect('urlproduto')

def editarProduto(request, id):
    produto = get_object_or_404(Produto, id=id)  
    #Produto.objects.get(id=id)

    if request.method == "GET":
        context = {'p': produto}
        return render(request, "editarProduto.html", context)
    else:
        thisnome = request.POST.get('txtNome')
        thispreco = request.POST.get('txtPreco').replace(',', '.')
        thisqtde = request.POST.get('txtQtde')
        thisdata = request.POST.get('txtData')
        thisdescricao = request.POST.get('txtDescricao')

        produto.nome = thisnome
        produto.preco = float(thispreco)
        produto.qtde = thisqtde
        produto.data = thisdata
        produto.descricao = thisdescricao

        produto.save()
        return redirect('urlproduto')

def excluirProduto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('urlproduto')

def entrar(request):
    if request.method == "GET":
        return render(request, "entrar.html")
    elif request.method == "POST":
        usuario = request.POST.get("txtUser")
        senha = request.POST.get("txtPass")
        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
            return redirect('urlindex')
        messages.error(request, "Falha na autenticação!")    
        return render(request, 'entrar.html')

def sair(request):
    logout(request)
    return redirect('urlentrar')

def cadastrarUsuario(request):
    if request.method == "GET":
        form = UsuarioForm()
        context = {'form': form}
        return render(request, 'cadastrarUsuario.html', context)
    else:
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('urlentrar')

def carrinho(request):
    carrinho = Carrinho(request)
    return render(request, 'carrinho.html', {'carrinho': carrinho})

def addcarrinho(request, id):
    produto = get_object_or_404(Produto, id=id)
    carrinho = Carrinho(request)
    carrinho.adicionar(produto=produto)
    return redirect('carrinho.html')

def delcarrinho(request):
    return HttpResponse('del carrinho')

def finalizarCompra(request):
    return HttpResponse('finalizar compra')
    