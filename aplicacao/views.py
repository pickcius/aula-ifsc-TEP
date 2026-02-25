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
    thisnome = request.POST.get('txtNome')
    thispreco = request.POST.get('txtPreco')
    thisqtd = request.POST.get('txtQtd')
    thisdata = request.POST.get('txtData')
    thisdescricao = request.POST.get('txtDescricao')

    produto = Produto(
        nome = thisnome,
        preco = float( thispreco ),
        qtd = thisqtd,
        data = thisdata,
        descricao = thisdescricao 
    )

    produto.save()
    return redirect('urlproduto')

    def editarProduto(request, id):
        produto = Produto.objects.get(id=id)

        thisnome = request.POST.get('txtNome')
        thispreco = request.POST.get('txtPreco')
        thisqtd = request.POST.get('txtQtd')
        thisdata = request.POST.get('txtData')
        thisdescricao = request.POST.get('txtDescricao')

        produto = Produto(
        nome = thisnome,
        preco = float( thispreco ),
        qtd = thisqtd,
        data = thisdata,
        descricao = thisdescricao 
    )





