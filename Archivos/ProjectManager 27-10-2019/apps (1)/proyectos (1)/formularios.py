"""Formulario de proyectos"""
#Django
from django import forms

# Models
from .models import Proyecto


class ProyectoForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Proyecto
        fields = ( 'nombre', 'estado', 'fase')#'perfil_lider',