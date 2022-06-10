
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

from . import views
from products.views import ProductListView


urlpatterns = [
    path('', ProductListView.as_view(), name="home"),    
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('ubication', views.ubication, name="ubication"),
    path('contacto', views.contacto, name="contacto"),
    path('register', views.register, name="register"),
    path('productos/', include('products.urls'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)