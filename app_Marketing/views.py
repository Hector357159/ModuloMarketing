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
    return redirect('/')
#pranififar evento
@login_required
def planidicar_evento(request):
    if request.method == 'POST':
        #obtener los datos del form avente
        nombre_evento = request.POST.get('Nombre')
        fecha_evento = request.POST.get('Fecha')
        musica = request.POST.get('Musica')
        comida = request.POST.get('Comida')
        actividad_recreativa = request.POST.get('Actividades')
        
        #creamos una instancia del modelo evento con los datos recibidos y los guarda en BD
        nuevo_evento = models.Evento.objects.create(
            nombreEvento = nombre_evento,
            fechaRealizacion=fecha_evento,
            musica=musica,
            comida=comida,
            actividadRecreativa=actividad_recreativa
        )
        
        #g# Guarda la instancia en la base de datos
        nuevo_evento.save()
        return redirect('Ver_eventos_campania')
    else:
        return render(request,'Planificar_evento.html',{
        'current_page': 'Planificar_evento',
        
        })
        


@login_required
def elaborar_campania(request):
    data = models.Evento.objects.all()
    return render(request,'Elaborar_campania.html',{
        'current_page': 'Elaborar_campania',
        
    })
@login_required
def ver_eventos_campania(request):
    return render(request,'ver_eventos_campania.html',{
        'current_page': 'Ver_eventos_campania',
    })