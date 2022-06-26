from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombre_familiar = models.CharField(max_length=50)
    edad_familiar = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)



    