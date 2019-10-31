"""Users URLs."""

# Django
from django.urls import path

# View
from . import views


urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='create/',
        view=views.CreateView.as_view(),
        name='create'
    ),
    path(
       route='me/perfil/',
        view=views.VistaUpdatePerfil.as_view(),
        name='update'
    ), 
   
    # Proyectos
    path(
        route='<str:username>/',
        view=views.VistaDetallesUsuario.as_view(),
        name='detail'
    )

]
