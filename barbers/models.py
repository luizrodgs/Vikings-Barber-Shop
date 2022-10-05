from django.db import models


class Barber(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, primary_key=True)

    def __str__(self):
        return self.name
