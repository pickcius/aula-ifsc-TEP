from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Produto

def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas'}
    return render(request, 'index.html', context)

def contato(request):
    context = {'nome': 'Instituto Federal de SC', 'telefone': '(47) 3363-5251', 'email': 'contato@ifsc.edu.br'}
    return render(request, 'contato.html', context)

def produto(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "produto.html", context)

def cadastrarProduto(request):
    return render(request, "cadastrarProduto.html")

def salvarProduto(request):
    thisnome = requeste.POST.get('txtNome')
    thispreco = request.POST.get('txtPreco')
    thisqtd = request.POST.get('txtQtd')
    thisdata = request.POST.get('txtData')
    thisdescricao = request.POST.get('txtDescricao')

    print(thisnome)

    produto = Produto(
        nome = thisnome
        preco = thispreco
        data = thisdata
        descricao = thisdescricao 
    )

    produto.save()
    return redirect('urlproduto')
