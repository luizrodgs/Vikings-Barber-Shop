from django.db import models


class Barber(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.name

    def show_cpf(self):
        formattedCpf = f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        return formattedCpf
