# Generated by Django 5.2.1 on 2025-05-15 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambientes',
            name='descricao',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ambientes',
            name='ni',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='ambientes',
            name='responsavel',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ambientes',
            name='sig',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='historico',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='historico',
            name='valor',
            field=models.FloatField(max_length=4),
        ),
    ]
