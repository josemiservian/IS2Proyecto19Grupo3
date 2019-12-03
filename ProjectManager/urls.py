# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
"""ProjectManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



urlpatterns = [

    path('admin/', admin.site.urls),

    #path('', include(('posts.urls', 'posts'), namespace='posts')),
    path('usuarios/', include(('apps.usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('', include(('apps.proyectos.urls', 'proyectos'), namespace='proyectos')),
    path('lineasBase/', include(('apps.lineasBase.urls', 'lineasBase'), namespace='lineasBase')),
    path('item/', include(('apps.items.urls', 'item'), namespace='item')),
   # path('item/', include(('apps.items.urls', 'item')))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)