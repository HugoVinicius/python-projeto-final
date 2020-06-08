from django.db import models

class ContasPagar(models.Model):
    nome = models.CharField(max_length=200)
    valor = models.FloatField()
    data_vencimento = models.DateField(null = True)
    data_pagamento = models.DateField(null = True)

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
    )

    CP_SITUACAO_CHOICES = [
        ('1', 'Pago'),
        ('2', 'A pagar'),
    ]
    
    situacao = models.CharField(
        max_length=4,
        choices=CP_SITUACAO_CHOICES,
    )
    dt_criacao = models.DateTimeField(auto_now_add=True)
