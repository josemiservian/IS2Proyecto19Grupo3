"""Fromularios de usuario."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from .models import Perfil
from apps.proyectos.models import Proyecto


class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username ya esta en uso.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Contrasenhas no coinciden.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        usuario = User.objects.create_user(**data)
        perfil = Perfil(usuario=usuario)
        perfil.save()

class AddUserForm(forms.ModelForm):
    """Crear usuario y asignarlo a un proyecto"""
    
    model = Perfil
    fields = (
        'usuario__email',
        'usuario__username',
        'usuario__first_name',
        'usuario__last_name',
        'proyecto_involucrado',
        'rol',
        'estado',
        'telefono',
        'direccion'

    )