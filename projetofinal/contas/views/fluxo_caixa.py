from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from ..models import ContasPagar
from ..models import ContasReceber

@csrf_exempt
@require_http_methods(["GET"])
def fluxocaixa(request):
    data = {}
    data['listaContas'] = ContasPagar.objects.all()

    return render(request, 'contas/fluxocaixa.html', data)
