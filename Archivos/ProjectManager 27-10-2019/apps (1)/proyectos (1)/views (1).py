
# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, FormView

# Forms
from .formularios import ProyectoForm

# Models
from .models import Proyecto


class ProjectsFeedView(LoginRequiredMixin, ListView):
    """Todos los proyectos del usuario."""

    template_name = 'proyectos/feed.html'
    model = Proyecto
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'proyectos'


class ProjectDetailView(LoginRequiredMixin, DetailView):
    """Detalles del proyecto"""

    template_name = 'proyectos/detail.html'
    queryset = Proyecto.objects.all()
    context_object_name = 'proyecto'


class CreateProjectView(LoginRequiredMixin, FormView):
    """Crea un nuevo proyecto."""

    template_name = 'proyectos/new.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('proyectos:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        #context['usuario'] = self.request.usuario
        #context['perfil'] = self.request.usuario.perfil
        #context['perfil_lider'] = self.request.usuario.perfil
        #print(context)
        return context
    
    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)