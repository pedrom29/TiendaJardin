from django.urls import path
from .views import home, producto, login, ubication, contacto, register

urlpatterns = [
<<<<<<< Updated upstream
    path('', home, name="home"),
    path('producto', producto, name="producto"),
    path('login', login, name="login"),
    path('ubication', ubication, name="ubication"),
    path('contacto', contacto, name="contacto"),
    path('register', register, name="register")
]
=======
    path('', ProductListView.as_view(), name="home"),    
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('ubication', views.ubication, name="ubication"),
    path('contacto', views.contacto, name="contacto"),
    path('register', views.register, name="register"),
    path('productos/', include('products.urls')),
    path('api/', include('rest_jardin.urls')),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> Stashed changes
