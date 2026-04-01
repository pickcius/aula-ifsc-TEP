from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    preco = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    qtde = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    telefone = models.CharField(max_length=25, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.PositiveIntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=50, null=True, blank=True)
    cliente = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Perfil de {self.cliente.username}'

class Venda(models.Model):
    STATUS_CHOICES = (
        ('P', 'PENDENTE'),
        ('C', 'CONCLUIDA'),
        ('X', 'CANCELADA')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    data = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Venda {self.id} - {self.cliente.username} ({self.get_status_display()})'

    @property
    def total(self):
        total = 0
        for item in self.itemvenda_set_all():
            total += item.produto.preco * item.qtde
        return total

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.produto.nome}'

    @property
    def subtotal(self):
        return self.produto.preco * self.qtde



