from django.shortcuts import render,redirect
from .forms import FormularioCadastroFuncionario,FormularioCadastroEmpresa
from .models import formularioFuncionario,formularioEmpresa
from django.views.generic import ListView

def home(request):
    return render(request,'index.html')



def CadastroFuncionarios(request): # mostrar o formulario baseado no modelo na pagina de html
    form = FormularioCadastroFuncionario(request.POST)
    if form.is_valid():
        form.save()
        return redirect('ListaFuncionario')
    else:
        form = FormularioCadastroFuncionario()
        return render(request,'CadastroFuncionario.html',{'form':form})

def CadastroEmpresa(request):
    form = FormularioCadastroEmpresa(request.POST)
    if form.is_valid():
        form.save()
        return redirect('ListaEmpresa')
    else:
        form = FormularioCadastroEmpresa()
        return render(request,'CadastrarEmpresa.html',{'form':form})


class lista(ListView):
    template_name = 'ListaDeFuncionarios.html'
    model = formularioFuncionario
    context_object_name = 'funcionarios'
    queryset = formularioFuncionario.objects.all()

class listaEmpresa(ListView):
    template_name = 'ListaDeEmpresas.html'
    model = formularioEmpresa
    context_object_name = 'empresas'
    queryset = formularioEmpresa.objects.all()


def Sair(request):
    return render(request,'Login.html')