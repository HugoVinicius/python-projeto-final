from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
@require_http_methods(["GET"])
def home(request):
	return render(request, 'contas/home.html')
