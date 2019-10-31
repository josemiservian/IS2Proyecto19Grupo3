#Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    """ Modelo de Item"""
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    perfil = models.ForeignKey('usuarios.Perfil', null=True, on_delete=models.CASCADE)
    linea_base = models.ForeignKey('lineasBase.LineaBase', null=True, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=30, null=False)
    tipo_item = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(null=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by {}'.format(self.nombre, self.usuario.username)