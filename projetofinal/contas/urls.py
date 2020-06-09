from django.urls import path

from .views import home as hv
from .views import contas_pagar as cpv
from .views import contas_receber as crv
from .views import relatorio as rv
from .views import fluxo_caixa as fv

urlpatterns = [
	path('', hv.home, name="home"),
	path('pagamento/listar', cpv.listar, name="listar_pagamento"),
    path('pagamento/cadastrar', cpv.cadastrar, name="cadastrar_pagamento"),
	path('pagamento/atualizar/<int:pk>/', cpv.atualizar, name="atualizar_pagamento"),
	path('pagamento/excluir/<int:pk>/', cpv.excluir, name="excluir_pagamento"),
	path('recebimento/listar', crv.listar, name="listar_recebimento"),
    path('recebimento/cadastrar', crv.cadastrar, name="cadastrar_recebimento"),
	path('recebimento/atualizar/<int:pk>/', crv.atualizar, name="atualizar_recebimento"),
	path('recebimento/excluir/<int:pk>/', crv.excluir, name="excluir_recebimento"),	
	path('relatorio/', rv.relatorio, name="relatorio"),	
	path('fluxocaixa/', fv.fluxocaixa, name="fluxo_caixa"),	
]