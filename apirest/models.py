from django.db import models

class Sensores(models.Model):
    temperatura = models.FloatField()
    humedad = models.FloatField()
    peso = models.FloatField()

class Lecturas(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
