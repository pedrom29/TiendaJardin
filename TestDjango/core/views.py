from contextlib import redirect_stderr
from itertools import product
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .forms import RegisterForm
from products.models import Product


# Create your views here.

def index(request):

    products = Product.objects.all().order_by('-id')


    return render(request, 'core/index.html', {
        'message': 'Listado de productos',
        'title': 'Productos',
        'products': products,
    })
    

def producto(request):
    return render(request, 'core/producto.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def ubication(request):
    return render(request, 'core/ubication.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        

        user = form.save()
        if user:
            messages.success(request, 'Usuario registrado exitosamente')
            return redirect('home')

    return render(request, 'core/register.html', {
        'form': form
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user :
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña no valido')          
        

    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect('login')

