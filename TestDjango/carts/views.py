from django.shortcuts import render
from .models import Product
from .utils import get_or_create_cart
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def cart(request):   
    cart = get_or_create_cart(request)
    

    return render(request, 'carts/cart.html', {
        'cart': cart
    })
# Create your views here.

def add(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.add(product)

    return render(request, 'carts/add.html', {
        'product': product
    })

def remove(request):
    
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')