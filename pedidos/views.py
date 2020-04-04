from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from .buildroute import build_route

from .models import Pedido

import datetime

# Create your views here.

def index(request):
    noentregados = Pedido.objects.filter(entregado=False)
    entregados = Pedido.objects.filter(entregado=True)
    now = timezone.now()
    
    context = {'entregados':entregados , 'noentregados':noentregados}
    return render(request, 'pedidos/index.html', context)

def routeurl(request):
    ubicacion = list(request.POST['ubicacion'].split(','))
    pedidos = Pedido.objects.filter(entregado=False).values()
    direcciones = [pedido['direccion'] for pedido in pedidos]
    finalurl = build_route(ubicacion,direcciones)
    context = {'finalurl':finalurl}
    if finalurl[0] == 'N':
        return render(request, 'pedidos/routeurl.html', context)
    else:
        return HttpResponseRedirect(finalurl)

def addpedido(request):
    context = {}
    return render(request, 'pedidos/addpedido.html', context)

