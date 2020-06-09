from django.urls import path

from .views import contas_pagar as cpv

urlpatterns = [
	path('', cpv.home, name="home"),
	path('listarpagamento', cpv.listar, name="listar_pagamento"),
    path('cadastrarpagamento/', cpv.cadastrar, name="cadastrar_pagamento"),
	path('atualizarpagamento/<int:pk>/', cpv.atualizar, name="atualizar_pagamento"),
	path('excluirpagamento/<int:pk>/', cpv.excluir, name="excluir_pagamento")	
]