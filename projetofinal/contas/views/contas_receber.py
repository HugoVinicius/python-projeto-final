from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from ..models import ContasReceber
from ..forms.contasreceber_form import ContasReceberForm

@csrf_exempt
@require_http_methods(["POST","GET"])
def listar(request):
	data = {}
	data['listaContas'] = ContasReceber.objects.all()

	return render(request, 'contas/contasReceberRead.html', data)

def cadastrar(request):
    data = {}
    form = ContasReceberForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_recebimento')

    data['operacao'] = 'Cadastro de Contas a Receber'
    data['form'] = form
    return render(request, 'contas/contasReceberCreateUpdate.html', data)

def atualizar(request, pk):	
    data = {}
    conta = ContasReceber.objects.get(id=pk)
    form = ContasReceberForm(request.POST or None, instance=conta)

    if form.is_valid():
        form.save()
        return redirect('listar_recebimento')

    data['operacao'] = 'Atualização de Contas a Receber'
    data['form'] = form
    return render(request, 'contas/contasReceberCreateUpdate.html', data)

def excluir(request, pk):
	try:
		conta = ContasReceber.objects.get(id=pk)
		conta.delete()		
		return redirect('listar_recebimento')
	except ObjectDoesNotExist:
		return redirect('listar_recebimento')

