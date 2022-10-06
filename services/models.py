from django.db import models


class Service(models.Model):
    service = models.CharField(max_length=50, unique=True)
    price = models.FloatField()

    def __str__(self):
        return self.service
