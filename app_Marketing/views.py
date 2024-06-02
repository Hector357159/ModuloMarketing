from django.shortcuts import render
#responde con http
from django.http import HttpResponse
#importamo render para mostrar archivos temporales
# Create your views here.

#creamos las funciones que se mostraran al cliente
def hello(request):
    return HttpResponse("Hello")

def login(request):
    return render(request, 'login.html')

def mercado(request):
    return render(request,'Mercado.html')

def planidicar_evento(request):
    return render(request,'Planificar_evento.html')

def elaborar_campania(request):
    return render(request,'Elaborar_campania.html')

def ver_eventos_campania(request):
    return render(request,'ver_eventos_campania.html')