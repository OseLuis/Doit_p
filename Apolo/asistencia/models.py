# asistencia/models.py (Fragmento importante, no el archivo completo)

from django.db import models
from django.contrib.auth.models import AbstractUser

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    class Meta:
        ordering = ['nombre'] # Para ordenar por nombre
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
    def __str__(self):
        return self.nombre

class CustomUser(AbstractUser):
    tipo_usuario_choices = [
        ('usuario', 'Usuario'),
        ('experto', 'Experto'),
    ]
    # Campos adicionales de tu CustomUser
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=20, choices=tipo_usuario_choices, default='usuario')
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    numDoc = models.CharField(max_length=100, unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fechaNacimiento = models.DateField(blank=True, null=True)
    # email ya está en AbstractUser pero es importante que lo manejes
    # evidenciaTrabajo y experienciaTrabajo para Expertos
    evidenciaTrabajo = models.CharField(max_length=200, blank=True, null=True)
    experienciaTrabajo = models.TextField(blank=True, null=True) # Textfield es mejor para textos largos
    hojaVida = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.username