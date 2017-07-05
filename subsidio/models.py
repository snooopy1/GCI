from django.db import models

# Create your models here.
class Subsidio(models.Model):
		Cod_cliente = models.IntegerField(primary_key=True)
		Dummy = models.IntegerField()
		Nombre = models.CharField(max_length=100)
		Fecha = models.DateField()
		Plazo = models.IntegerField()
		SubsidioEntregado = models.FloatField()
		SubsidioUtilizado = models.FloatField()
		SubsidioDisponible = models.FloatField()