from django.urls import path

from .views import home,CadastroFuncionarios,lista,CadastroEmpresa,listaEmpresa,Sair
urlpatterns=[
        path('',home,name='Pagina Principal'),
        path('/cadastro',CadastroFuncionarios,name='CadastroFuncionario'),
        path('/lista',lista.as_view(),name='ListaFuncionario'),
        path('/cadastroEmpresa',CadastroEmpresa,name='CadastroEmpresa'),
        path('/listaEmpresas',listaEmpresa.as_view(),name = 'ListaEmpresa'),
        path('Sair',Sair,name = 'Sair'),


    ]