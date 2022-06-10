from django.urls import path
from .views import home, producto, login, ubication, contacto, register

urlpatterns = [
    path('', home, name="home"),
    path('producto', producto, name="producto"),
    path('login', login, name="login"),
    path('ubication', ubication, name="ubication"),
    path('contacto', contacto, name="contacto"),
    path('register', register, name="register")
]