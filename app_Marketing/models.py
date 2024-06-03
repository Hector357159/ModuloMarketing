from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    nombreEvento = models.CharField(max_length=100)
    fechaRealizacion = models.DateField(blank=True, null=True)
    musica = models.CharField(max_length=100)
    cominda = models.CharField(max_length=100)
    actividadRecreativa = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nombreEvento
#modelo de REdes Sociales
class RedesSociales(models.Model):
    nombreRedSocia = models.CharField(max_length=100)
    seguidores = models.PositiveBigIntegerField()
    def __str__(self):
        return self.nombreRedSocia
#modelo de  Evento 
class Campania(models.Model):
    nombreCampania = models.CharField(max_length=100)
    fechaInicio = models.DateField(blank=True, null=True)
    fechaFinal = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True) 
    imagen = models.ImageField(blank=True)
    presupuesto = models.PositiveIntegerField()
    campania= models.ForeignKey(Evento, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombreCampania


#modelos de Estadistica
class Estadistica(models.Model):
    redSocial = models.ForeignKey(RedesSociales, on_delete=models.CASCADE)
    campania = models.ForeignKey(Campania , on_delete=models.CASCADE)
    seguidores = models.PositiveIntegerField()
    edad = models.PositiveBigIntegerField()
    departamento = models.CharField(max_length=100)
    meGusta = models.PositiveBigIntegerField()
    
    def __str__(self) -> str:
        return self.redSocial
