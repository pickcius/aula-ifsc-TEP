from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    preco = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    qtde = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    data = models.DateField(null=True, blank=True)