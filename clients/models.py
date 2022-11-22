from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.name

    def show_cpf(self):
        formattedCpf = f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        return formattedCpf

    def show_phone(self):
        formattedPhone = f"{self.phone[0:2]} 9 {self.phone[3:7]}-{self.phone[7:]}"
        return formattedPhone
