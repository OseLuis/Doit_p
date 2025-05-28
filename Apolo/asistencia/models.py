<<<<<<< HEAD
# asistencia/models.py
=======
# asistencia/models.py (Fragmento importante, no el archivo completo)
>>>>>>> origin/master

from django.db import models
from django.contrib.auth.models import AbstractUser

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    class Meta:
<<<<<<< HEAD
        ordering = ['nombre']
=======
        ordering = ['nombre'] # Para ordenar por nombre
>>>>>>> origin/master
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
    def __str__(self):
        return self.nombre

class CustomUser(AbstractUser):
    tipo_usuario_choices = [
<<<<<<< HEAD
        ('usuario', 'Usuario Normal'), # Cambié "Usuario" a "Usuario Normal" para más claridad
=======
        ('usuario', 'Usuario'),
>>>>>>> origin/master
        ('experto', 'Experto'),
    ]
    # Campos adicionales de tu CustomUser
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=20, choices=tipo_usuario_choices, default='usuario')
    nacionalidad = models.CharField(max_length=100, blank=True, null=True)
    numDoc = models.CharField(max_length=100, unique=True, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fechaNacimiento = models.DateField(blank=True, null=True)
<<<<<<< HEAD
    evidenciaTrabajo = models.CharField(max_length=200, blank=True, null=True)
    experienciaTrabajo = models.TextField(blank=True, null=True)
    hojaVida = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.username

    # Métodos de conveniencia para usar en las plantillas (opcional, pero buena práctica)
    def is_usuario_normal(self):
        """Retorna True si el usuario tiene el rol 'usuario'."""
        return self.tipo_usuario == 'usuario'

    def is_experto(self):
        """Retorna True si el usuario tiene el rol 'experto'."""
        return self.tipo_usuario == 'experto'
=======
    # email ya está en AbstractUser pero es importante que lo manejes
    # evidenciaTrabajo y experienciaTrabajo para Expertos
    evidenciaTrabajo = models.CharField(max_length=200, blank=True, null=True)
    experienciaTrabajo = models.TextField(blank=True, null=True) # Textfield es mejor para textos largos
    hojaVida = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.username
>>>>>>> origin/master
