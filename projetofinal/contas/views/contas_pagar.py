from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from ..models import ContasPagar
from ..forms.contaspagar_form import ContasPagarForm

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	data = {}
	data['listaContas'] = ContasPagar.objects.all()

	return render(request, 'contas/contasPagarRead.html', data)

def cadastrar(request):
    data = {}
    form = ContasPagarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_pagamento')

    data['operacao'] = 'Cadastro de Contas a Pagar'
    data['form'] = form
    return render(request, 'contas/contasPagarCreateUpdate.html', data)

def atualizar(request, pk):	
    data = {}
    conta = ContasPagar.objects.get(id=pk)
    form = ContasPagarForm(request.POST or None, instance=conta)

    if form.is_valid():
        form.save()
        return redirect('listar_pagamento')

    data['operacao'] = 'Atualização de Contas a Pagar'
    data['form'] = form
    return render(request, 'contas/contasPagarCreateUpdate.html', data)

def excluir(request, pk):
	try:
		conta = ContasPagar.objects.get(id=pk)
		conta.delete()		
		return redirect('listar_pagamento')
	except ObjectDoesNotExist:
		return redirect('listar_pagamento')

