from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    document_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

class Sede(models.Model):
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} / {self.address}"

class Mesa(models.Model):
    capacity = models.IntegerField()
    zone = models.CharField(max_length=45)

    def __str__(self) -> str:
        return f"{self.capacity} / {self.zone}"

class Reserva(models.Model):
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.cliente.name} - {self.sede.name}"