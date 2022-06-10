from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/index.html')
    

def producto(request):
    return render(request, 'core/producto.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def ubication(request):
    return render(request, 'core/ubication.html')

def register(request):
    return render(request, 'core/register.html')

def login(request):
    return render(request, 'core/login.html')
