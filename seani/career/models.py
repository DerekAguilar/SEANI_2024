from django.db import models

# Create your models here.
class Career(models.Model):
    LEVELS=[
        ('TSU','Técnico Superior Universitario'),
        ('Ing','Ingeniería'),
        ('Lic','Licenciatura'),
        ('M','Maestría')
    ]

    name=models.CharField(
        verbose_name='Nombre',
        max_length=200,
    )
    short_name=models.CharField(
        verbose_name='Abreviatura',
        max_length=10,
    )
    level=models.CharField(
        verbose_name='Nivel',
        max_length=10,
        choices=LEVELS,
    )