from django.db import models

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14)
    nasc = models.CharField(max_length=10)
    sexo = models.CharField(max_length=10)
    ddd = models.CharField(max_length=2)
    telefone = models.CharField(max_length=13)
    email = models.CharField(max_length=40)