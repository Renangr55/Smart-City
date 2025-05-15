from django.db import models


# Create your models here.
class Sensores(models.Model):
    SENSOR_CHOICES = [
        ('Temperatura','Temperatura (°C)'),
        ('Luminosidade', 'Luminiosidade (lux)'),
        ('Umidade', 'Umidade (%)'),
        ('Contador','Contador (num)')
    ]
    sensor = models.CharField(choices=SENSOR_CHOICES)
    mac_address = models.CharField(max_length=60, blank=False)
    unidade_med = models.CharField(max_length=17,blank=False)
    latitude = models.FloatField(max_length=10, blank=False)
    longitude = models.FloatField()
    status = models.BooleanField()

class Ambientes(models.Model):
    sig = models.IntegerField(blank=False)
    descricao = models.CharField(max_length=200,blank=True, null=True)
    ni = models.CharField(max_length=7, blank=False)
    responsavel = models.CharField(max_length=100,blank=True)

class Historico(models.Model):
    tipo_sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE)
    valor = models.FloatField(max_length=4)
    timestamp = models.DateTimeField()

    
