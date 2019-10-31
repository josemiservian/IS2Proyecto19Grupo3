"""Projects URLs."""

# Django
from django.urls import path

# Views
from . import views

urlpatterns = [

    path(
        route='',
        view=views.ProjectsFeedView.as_view(),
        name='feed'
    ),

    path(
        route='proyectos/new/',
        view=views.CreateProjectView.as_view(),
        name='create'
    ),

    path(
        route='proyectos/<int:pk>/',
        view=views.ProjectDetailView.as_view(),
        name='detail'
    )
]