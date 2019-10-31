# Django
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Proyecto(models.Model):
    """Modelo de Proyecto"""
    nombre = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=20, null=False)
    fase = models.CharField(max_length=20, null=False)

    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #perfil_lider = models.ForeignKey('usuarios.Perfil', null=True, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre