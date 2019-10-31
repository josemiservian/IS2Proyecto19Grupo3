from django.db import models

# Create your models here.
class Permiso(models.Model):
    """docstring for Permiso"""
    nombre = models.CharField(max_length=30, null=False)
    nivel = models.IntegerField(null=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre