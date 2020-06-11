from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from ..models import ContasPagar
from ..models import ContasReceber

@csrf_exempt
@require_http_methods(["GET", "POST"])
def relatorioPagar(request):
    data = {}

    dataFiltro = request.POST.get('datafiltro', '')

    data['data_busca'] = ""    
    if (dataFiltro != ""):
        dataFiltro = datetime.strptime(dataFiltro, '%Y-%m-%d').date()
        data['data_busca'] = '%s-%s-%s' % (dataFiltro.strftime("%Y"), dataFiltro.strftime("%m"), dataFiltro.strftime("%d"))
   
    data['url'] = '/relatoriopagar/';
    data['titulo'] = 'Relatório de Contas a Pagar'
    data['descricaofiltro'] = 'Data de vencimento:'
    data['tipo'] = 'pagar'
    
    somaTotal = 0

    if (dataFiltro != ""):  
        listaContasPagar = ContasPagar.objects.filter(situacao=2, data_vencimento__startswith=dataFiltro)

        for contaPagar  in listaContasPagar:
            contaPagar.data_vencimento = '%s/%s/%s' % (contaPagar.data_vencimento.strftime("%d"), contaPagar.data_vencimento.strftime("%m"), contaPagar.data_vencimento.strftime("%Y"))
            contaPagar.data_pagamento =  '%s/%s/%s' % (contaPagar.data_pagamento.strftime("%d"), contaPagar.data_pagamento.strftime("%m"), contaPagar.data_pagamento.strftime("%Y"))
            somaTotal = somaTotal + contaPagar.valor
        
        data['listaContas'] = listaContasPagar
    else:
        data['listaContas'] = []

    data['valorTotal'] = somaTotal

    return render(request, 'contas/relatorio.html', data)    

@csrf_exempt
@require_http_methods(["GET", "POST"])
def relatorioReceber(request):
    data = {}

    dataFiltro = request.POST.get('datafiltro', '')

    data['data_busca'] = ""
    if (dataFiltro != ""):
        dataFiltro = datetime.strptime(dataFiltro, '%Y-%m-%d').date()
        data['data_busca'] = '%s-%s-%s' % (dataFiltro.strftime("%Y"), dataFiltro.strftime("%m"), dataFiltro.strftime("%d"))
   
    data['url'] = '/relatorioreceber/';
    data['titulo'] = 'Relatório de Contas a Receber'
    data['descricaofiltro'] = 'Data da expectativa:'
    data['tipo'] = 'receber'
    
    somaTotal = 0

    if (dataFiltro != ""):  
        listaContasReceber = ContasReceber.objects.filter(situacao=2, data_expectativa__startswith=dataFiltro)

        for contaReceber  in listaContasReceber:
            contaReceber.data_expectativa = '%s/%s/%s' % (contaReceber.data_expectativa.strftime("%d"), contaReceber.data_expectativa.strftime("%m"), contaReceber.data_expectativa.strftime("%Y"))
            contaReceber.data_recebimento =  '%s/%s/%s' % (contaReceber.data_recebimento.strftime("%d"), contaReceber.data_recebimento.strftime("%m"), contaReceber.data_recebimento.strftime("%Y"))
            somaTotal = somaTotal + contaReceber.valor
        
        data['listaContas'] = listaContasReceber
    else:
        data['listaContas'] = []

    data['valorTotal'] = somaTotal

    return render(request, 'contas/relatorio.html', data)    