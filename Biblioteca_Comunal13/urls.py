"""
URL configuration for Biblioteca_Comunal13 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # API V1
    path('usuarios/', include('apps.usuarios.urls')),
    path('autores/', include('apps.autores.urls')),
    path('categorias/', include('apps.categorias.urls')),
    path('libros/', include('apps.libros.urls')),
    path('prestamos/', include('apps.prestamos.urls')),
    path('empleados/', include('apps.empleados.urls')),
    path('editoriales/', include('apps.editoriales.urls')),
]