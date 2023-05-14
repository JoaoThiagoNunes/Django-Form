from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('='*40)
            print('Mensagem recebida')
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            print('='*40)

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm
        else:
            messages.error(request, 'Erro ao enviar o e-mail!')

    context = {
        'form': form
    }
    return render(request, 'contato.html',context)