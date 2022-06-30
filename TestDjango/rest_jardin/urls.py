from django.urls import path
from rest_jardin.views import lista_products

urlpatterns = [
    path('lista_products', lista_products, name="lista_products")
]