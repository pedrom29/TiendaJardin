from django.db import models

# Create your models here.

class Product(models.Model):
    idProduct = models.IntegerField(primary_key=True, verbose_name="Id de producto")
    name = models.CharField(max_length=200, verbose_name="Nombre producto")
    
    def __str__(self):
        return self.name