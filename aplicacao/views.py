from django.shortcuts import render

def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas'}
    return render(request, 'index.html', context)

def contato(request):
    context = {'nome': 'Instituto Federal de SC', 'telefone': '(47) 3363-5251', 'email': 'contato@ifsc.edu.br'}
    return render(request, 'contato.html', context)
