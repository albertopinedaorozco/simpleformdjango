from django.db import models

class Mesero(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    observaciones = models.TextField(max_length=80)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=30)
    ingredientes = models.ForeignKey('Ingrediente', on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre






