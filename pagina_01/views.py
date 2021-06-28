from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import solo_admin
# Create your views here.
@solo_admin
def loginADMIN(request):
    return render(request, 'pagina_01/logeadoADMIN.html')
@solo_admin
def planificadorAdmin(request):
    return render(request,'pagina_01/planificadorADMIN.html')
def login(request):
    return render(request, 'pagina_01/logeado.html')

def planificador(request):
    return render(request,'pagina_01/planificador.html')

def saladechat(request):
    return render(request,'pagina_01/saladechat.html')

def videoconferencia(request):
    return render(request,'pagina_01/videoconferencias.html')
def comunicadosINDEX(request):
    return render(request, 'pagina_01/comunicadosINDEX.html')

def comunicados(request):
    return render(request, 'pagina_01/comunicados.html')

def organizaciones(request):
    return render(request,'pagina_01/organizaciones.html')

def perfil(request):
    return render(request, 'pagina_01/perfil.html')
def contacto(request):
    return render(request, 'pagina_01/contacto.html')
@solo_admin
def registro(request):
    data={
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            user=formulario.save()
            #autenticar al usuario y redirigir al inicio
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            login(request)
            messages.success(request,'cuenta creada con exito')

    return render(request, 'pagina_01/registro.html',data)