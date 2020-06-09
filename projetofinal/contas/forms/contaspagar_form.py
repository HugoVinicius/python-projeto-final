from django.views.generic import CreateView
from django.forms import ModelForm
from ..models import ContasPagar

class ContasPagarForm(ModelForm):
    class Meta:
        model = ContasPagar
        fields = ['nome', 'valor', 'data_vencimento', 'data_pagamento', 'classificacao', 'forma_pagamento', 'situacao']