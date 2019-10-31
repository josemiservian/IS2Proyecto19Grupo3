# Django
from django.db import models

# Create your models here.
class LineaBase(models.Model):
    """Modelo de Linea Base"""
    nombre = models.CharField(max_length=50, null=False)
    estado = models.CharField(max_length=20, null=False)

    proyecto = models.ForeignKey('proyectos.Proyecto', null=True, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
        