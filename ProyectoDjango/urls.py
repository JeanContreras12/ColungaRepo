"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from ColungaApp import views
from pagina_01 import views as viewsindex
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logeado/', login_required(viewsindex.login), name='logeado'),
    path('registro/',login_required(viewsindex.registro), name='registro'),
    path('accounts/login/',LoginView.as_view(template_name='ColungaApp/login.html'), name='login'),
    path('Inicio/',LogoutView.as_view(template_name='pagina_01/index.html'), name='inicio'),
    path('planificador/',login_required(LoginView.as_view(template_name='pagina_01/planificador.html')), name='planificador'),
    path('saladechat/',login_required(LoginView.as_view(template_name='pagina_01/saladechat.html')), name='saladechat'),
    path('videoconferencias/',login_required(LoginView.as_view(template_name='pagina_01/videoconferencias.html')), name='videoconferencias'),
    path('comunicados/',login_required(LoginView.as_view(template_name='pagina_01/comunicados.html')), name='comunicados'),
    path('organizaciones/',login_required(LoginView.as_view(template_name='pagina_01/organizaciones.html')), name='organizaciones'),
    path('perfil/',login_required(LoginView.as_view(template_name='pagina_01/perfil.html')), name='perfil'),


]
