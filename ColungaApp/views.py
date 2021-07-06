from django.shortcuts import render
def index(request): #pasamos un objeto de tipo request como primer argumento
    return render(request,'ColungaApp/index.html')


#def login(request):
    #return render(request,'ColungaApp/login.html')