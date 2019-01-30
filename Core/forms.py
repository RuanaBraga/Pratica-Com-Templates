from django import forms
from .models import formularioFuncionario,formularioEmpresa

class FormularioCadastroFuncionario(forms.ModelForm):
    class Meta:
        model = formularioFuncionario
        fields = ['nome','cpf','telefone','email']

class FormularioCadastroEmpresa(forms.ModelForm):
    class Meta:
        model = formularioEmpresa
        fields = ['razao_social','cnpj','telefone_comercial','endereço','email_comercial']


