# Generated by Django 5.2.1 on 2025-05-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_sensores_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensores',
            name='sensor',
            field=models.CharField(choices=[('Temperatura (°C)', 'Temperatura (°C)'), ('Luminosidade (lux)', 'Luminiosidade (lux)'), ('Umidade (%)', 'Umidade (%)'), ('Contador (num)', 'Contador (num)')]),
        ),
    ]
