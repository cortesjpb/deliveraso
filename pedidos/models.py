from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField('fecha de venta')
    direccion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    entregado = models.BooleanField()
    total = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.direccion
