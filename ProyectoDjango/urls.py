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
from pagina_01.views import UserEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logeado/', login_required(viewsindex.login), name='logeado'),
    path('registro/',login_required(viewsindex.registro), name='registro'),
    path('accounts/login/',LoginView.as_view(template_name='ColungaApp/login.html'), name='login'),
    path('',LogoutView.as_view(template_name='pagina_01/index.html'), name='inicio'),
    path('planificador/',login_required(viewsindex.planificador), name='planificador'),
    path('saladechat/',login_required(viewsindex.saladechat), name='saladechat'),
    path('videoconferencias/',login_required(viewsindex.videoconferencia), name='videoconferencias'),
    path('comunicados/',login_required(viewsindex.comunicados), name='comunicados'),
    path('comunicado/',viewsindex.comunicadosINDEX, name='comunicados'),
    path('organizaciones/',login_required(viewsindex.organizaciones), name='organizaciones'),

    path('edit_profile/',UserEditView.as_view(), name='edit_profile'),
    path('password/',auth_views.PasswordChangeView.as_view()),

    path('contacto/',login_required(viewsindex.contacto), name='contacto'),
    path('login-admin/',login_required(viewsindex.loginADMIN), name='login-admin'),
    path('planificadorADMIN/',login_required(viewsindex.planificadorAdmin), name='planificador'),
]
