from django.db import models

class ContasPagar(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_vencimento = models.DateField(null = True)
    data_pagamento = models.DateField(null = True)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    CP_CLASSIFICACAO_CHOICES = [
        ('1', 'Telecomunicações'),
        ('2', 'Água'),
        ('3', 'Energia'),
        ('4', 'Alimentação'),
        ('5', 'Outros'),
    ]

    classificacao = models.CharField(
        max_length=4,
        choices=CP_CLASSIFICACAO_CHOICES,
        default=1,
    )

    CP_FORMA_PAGAMENTO_CHOICES = [
        ('1', 'Boleto'),
        ('2', 'Crédito'),
        ('3', 'Débito'),
        ('4', 'Depósito'),
        ('5', 'Outros'),
    ]

    forma_pagamento = models.CharField(
        max_length=4,
        choices=CP_FORMA_PAGAMENTO_CHOICES,
        default=1,
    )

    CP_SITUACAO_CHOICES = [
        ('1', 'Pago'),
        ('2', 'A pagar'),
    ]
    
    situacao = models.CharField(
        max_length=4,
        choices=CP_SITUACAO_CHOICES,
        default=1,
    )

    class Meta:
        verbose_name_plural: 'ContasPagar'

    def __str__(self):
        return self.nome        
    
class ContasReceber(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    data_expectativa = models.DateField(null = True)
    data_recebimento = models.DateField(null = True)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    CR_CLASSIFICACAO_CHOICES = [
        ('1', 'Serviços Prestados'),
        ('2', 'Salario'),
        ('3', 'Vendas'),
        ('4', 'Outros'),
    ]

    classificacao = models.CharField(
        max_length=4,
        choices=CR_CLASSIFICACAO_CHOICES,
        default=1,
    )

    CR_FORMA_RECEBIMENTO_CHOICES = [
        ('1', 'Dinheiro'),
        ('2', 'Cheque'),
        ('3', 'Cartão Credito'),
        ('4', 'Cartão Debito'),
        ('5', 'Deposito'),
        ('6', 'Vale'),
        ('7', 'Outros'),
    ]

    forma_recebimento = models.CharField(
        max_length=4,
        choices=CR_FORMA_RECEBIMENTO_CHOICES,
        default=1,
    )

    CR_SITUACAO_CHOICES = [
        ('1', 'Recebido'),
        ('2', 'A receber'),
    ]
    
    situacao = models.CharField(
        max_length=4,
        choices=CR_SITUACAO_CHOICES,
        default=1,
    )

    class Meta:
        verbose_name_plural: 'ContasReceber'

    def __str__(self):
        return self.descricao