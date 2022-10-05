from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, primary_key=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name
