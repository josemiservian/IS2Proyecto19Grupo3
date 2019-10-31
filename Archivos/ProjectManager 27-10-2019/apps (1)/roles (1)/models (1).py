from django.db import models

# Create your models here.
class Rol(models.Model):
    """docstring for Rol"""
    nombre = models.CharField(max_length=30, null=False)

    permiso = models.ForeignKey('permisos.Permiso', null=True, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre 