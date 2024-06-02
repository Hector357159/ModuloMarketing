from django.shortcuts import render
#responde con http
from django.http import HttpResponse
#importamo render para mostrar archivos temporales
# Create your views here.

#creamos las funciones que se mostraran al cliente
def hello(request):
    return HttpResponse("Hello")

def login(request):
    return render(request, 'login.html',{
        'Curren_page': 'login',
    })

def mercado(request):
    return render(request,'Mercado.html',{
        'current_page': 'Mercado',
    })

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