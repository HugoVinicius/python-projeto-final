from django.urls import path

from .views import contas_pagar as cpv

urlpatterns = [
	path('', cpv.home, name="index"),
	# path('listar/', pv.listar, name="listar"),
	# path('detalhar/<int:id_pessoa>/', pv.detalhar, name="detalhar"),
	# path('excluir/<int:id_pessoa>/', pv.excluir, name="excluir"),
	# path('cadastrar/', pv.cadastrar, name="cadastrar")
]