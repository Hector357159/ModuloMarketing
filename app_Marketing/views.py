from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from . import models
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
#responde con http
from django.http import HttpResponse
#importamo render para mostrar archivos temporales
# Create your views here.

#creamos las funciones que se mostraran al cliente
def hello(request):
    return HttpResponse("Hello")
#requere de hacer login
def login(request):
    return render(request, 'registration/login.html',{
        'Curren_page': 'login',
    })


#reqiere login
@login_required
def mercado(request):
    return render(request,'Mercado.html',{
        'current_page': 'Mercado',
    })

#cerrar cesion
def exit(request):
    logout(request)
def planidicar_evento(request):
    return render(request,'Planificar_evento.html',{
        'current_page': 'Planificar_evento',
    })

def elaborar_campania(request):
    return render(request,'Elaborar_campania.html',{
        'current_page': 'Elaborar_campania',
    })

def ver_eventos_campania(request):
    return render(request,'ver_eventos_campania.html',{
        'current_page': 'Ver_eventos_campania',
    })