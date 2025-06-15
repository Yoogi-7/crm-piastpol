from django.db import models
from clients.models import Client, DeliveryAddress


class Distributor(models.Model):
    STATUS_CHOICES = [
        ('warehouse', 'Magazyn'),
        ('client', 'U klienta'),
        ('service', 'Serwis'),
        ('scrap', 'Złom'),
    ]

    OWNER_CHOICES = [
        ('piastpol', 'Piastpol'),
        ('lease', 'Dzierżawa'),
        ('client', 'Klient'),
    ]

    serial_number = models.CharField(max_length=50, unique=True)
    barcode = models.CharField(max_length=50, unique=True)
    device_type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='warehouse')
    owner = models.CharField(max_length=20, choices=OWNER_CHOICES, default='piastpol')
    installation_date = models.DateField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.serial_number} - {self.device_type}"
