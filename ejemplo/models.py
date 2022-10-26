from django.db import models

class Familiar(models.Model):
      nombre = models.CharField(max_length=100)
      direccion = models.CharField(max_length=200)
      numero_pasaporte = models.IntegerField()
      fecha_nacimiento = models.CharField(max_length=100)

      def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.fecha_nacimiento}, {self.id}"

