from django.views.generic import CreateView
from django.forms import ModelForm
from ..models import ContasReceber

class ContasReceberForm(ModelForm):
    class Meta:
        model = ContasReceber
        fields = ['descricao', 'valor', 'data_expectativa', 'data_recebimento', 'classificacao', 'forma_recebimento', 'situacao']