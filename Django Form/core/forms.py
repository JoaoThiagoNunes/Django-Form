from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, min_length=3)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    