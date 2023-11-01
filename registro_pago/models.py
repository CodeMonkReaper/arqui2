from django.db import models

class Pago(models.Model):
    cliente = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    rutCliente = models.CharField(max_length=12)
    fecha = models.DateField()
    descripcion = models.TextField()

class Reservas(models.Model):
    cliente = models.CharField(max_length=100)
    rutCliente = models.CharField(max_length=12)
    fecha = models.DateField()
    hora = models.TimeField()
    medico = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    motivoConsulta = models.TextField()