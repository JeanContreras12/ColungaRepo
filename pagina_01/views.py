from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
# Create your views here.

def login(request):
    return render(request, 'pagina_01/logeado.html')

def registro(request):
    data={
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autenticar al usuario y redirigir al inicio
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request)
            return redirect(to='inicio')

    return render(request, 'pagina_01/registro.html',data)