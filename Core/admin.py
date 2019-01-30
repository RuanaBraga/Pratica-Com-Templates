from django.contrib import admin

from .models import formularioEmpresa,formularioFuncionario

admin.site.register(formularioFuncionario)
admin.site.register(formularioEmpresa)