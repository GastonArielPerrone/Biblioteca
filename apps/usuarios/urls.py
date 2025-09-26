from operator import index
from django.contrib.auth import views as auth_views
from apps.usuarios.views import lista_usuarios, index
from django.urls import path

urlpatterns = [
    path('lista/', lista_usuarios, name='lista_usuarios'),
    path('', index, name='index'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
