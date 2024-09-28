from django.db import models

# Create your models here.

class Cliente(models.Model):
    cliente_id = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)

class Pedidos(models.Model):
    pedido_id = models.CharField(max_length=60)
    id_cliente = models.CharField(max_length=60)
    id_producto = models.CharField(max_length=60)
    Id_domiciliario = models.CharField(max_length=60)
