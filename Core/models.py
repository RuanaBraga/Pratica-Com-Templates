from django.db import models
from django.urls import reverse

class formularioFuncionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)






class formularioEmpresa(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=15)
    endereço = models.CharField(max_length=40)
    telefone_comercial = models.CharField(max_length=15)
    email_comercial = models.CharField(max_length=100)



  # ''' def get_absolute_url(self):
       # return reverse('AtualizaFuncionario',kwargs={'pk':self.pk})'''
#''' def get_absolute_url(self):
       # return reverse('AtualizaFuncionario',kwargs={'pk':self.pk})'''