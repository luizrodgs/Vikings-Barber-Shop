from django.db import models

from barbers.models import Barber
from clients.models import Client
from services.models import Service


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
