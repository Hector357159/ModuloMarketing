from django.urls import path
from . import views
urlpatterns = [
    #agregamos nuestras direcciones con nuestra respuesta o html o htmlresponse

    path('', views.mercado,name='Mercado'),
    #
    path('Planificar_evento/', views.planidicar_evento,name='Planificar_evento'),
    
    path('Ver_eventos_campania', views.ver_eventos_campania,name='Ver_eventos_campania'),
    
    path('Elaborar_campania/', views.elaborar_campania,name='Elaborar_campania'),
    
    path('salir/', views.exit,name='Exit'),
    
]
