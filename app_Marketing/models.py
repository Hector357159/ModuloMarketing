from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#modelo de REdes Sociales
class RedesSociales(models.Model):
    nombreRedSocia = models.CharField(max_length=100)
    seguidores = models.PositiveBigIntegerField()
    def __str__(self):
        return self.nombreRedSocia

#modelos de Estadistica
class Estadistica(models.Model):
    redSocial = models.OneToOneField(RedesSociales, on_delete=models.CASCADE)
    seguidores = models.PositiveIntegerField()
    edad = models.PositiveBigIntegerField()
    departamento = models.CharField(max_length=100)
    meGusta = models.PositiveBigIntegerField()
    
    def __str__(self) -> str:
        return self.redSocial

#modelo de  Evento 
class Campania(models.Model):
    nombreCampania = models.CharField(max_length=100)
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaFinal = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True) 
    imagen = models.ImageField(blank=True)
    presupuesto = models.PositiveIntegerField()
    estadistica = models.ForeignKey(Estadistica, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombreCampania

class Evento(models.Model):
    nombreEvento = models.CharField(max_length=100)
    fechaRealizacion = models.DateTimeField(auto_now_add=True)
    musica = models.CharField(max_length=100)
    cominda = models.CharField(max_length=100)
    actividadRecreativa = models.CharField(max_length=100)
    campania= models.ForeignKey(Campania, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombreEvento