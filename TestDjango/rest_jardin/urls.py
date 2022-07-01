from django.urls import path
from rest_jardin.views import lista_products, detalle_product

urlpatterns = [
    path('lista_products', lista_products, name="lista_products"),
    path('detalle_product/<int:id>', detalle_product, name="detalle_product")
]