from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'),
    path('api/', include('rest_jardin.urls')),
    
]