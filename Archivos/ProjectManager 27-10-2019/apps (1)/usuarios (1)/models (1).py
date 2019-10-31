# Django
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Perfil(models.Model):
    """Modelo de Perfil de usuario."""

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    proyecto_involucrado = models.ForeignKey('proyectos.Proyecto', null=True, on_delete=models.CASCADE)
    rol = models.ForeignKey('roles.Rol', null=True, on_delete=models.CASCADE)

    estado = models.CharField(max_length=20, null=False)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to='usuarios/imagenes',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #proyecto = 

    def __str__(self):
        """Return username."""
        #return '{}'.format(self.usuario.username)#, self.proyecto.nombre
        return self.usuario.username