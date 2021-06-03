from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def login(request):
    return render(request, 'pagina_01/logeado.html')

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
    else:
        form = UserCreationForm()
    context = { 'form' : form}
    return render(request, 'pagina_01/registro.html')