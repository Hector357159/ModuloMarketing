from django.urls import path
from . import views
urlpatterns = [
    #agregamos nuestras direcciones con nuestra respuesta o html o htmlresponse
    path('',views.login),
    
    path('mercado/', views.mercado),
    #
    path('Planificar_evento/', views.planidicar_evento),
    
    path('ver_eventos_campania', views.ver_eventos_campania),
    
    path('Elaborar_campania/', views.elaborar_campania),
    
]
