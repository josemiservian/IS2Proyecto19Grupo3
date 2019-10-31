"""Vista de Usuarios."""

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView, ListView
from django.http import HttpResponse
# Models
from django.contrib.auth.models import User
from apps.proyectos.models import Proyecto
from .models import Perfil

# Forms
from .formularios import SignupForm


class VistaDetallesUsuario(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'usuarios/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'usuario'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        usuario = self.get_object()
        context['proyectos'] = Proyecto.objects.filter(user=usuario).order_by('-created')
        return context


class SignupView(FormView):
    """Usuarios sign up view."""

    template_name = 'usuarios/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('usuarios:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class VistaUpdatePerfil(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'usuarios/update_profile.html'
    model = Perfil
    fields = ['estado', 'telefono', 'direccion', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.usuario.perfil

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.usuario.username
        return reverse('usuarios:detail', kwargs={'username': username})

class LoginView(auth_views.LoginView):
    """Login View"""
    
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('proyectos:feed')

    

class CreateView(FormView):#ver para heredar de signup nomas y cambiarle la succes url
    template_name = 'usuarios/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('proyectos:feed')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'usuarios/logged_out.html'
