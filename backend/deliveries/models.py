from django.db import models
from clients.models import Client, DeliveryAddress
from equipment.models import Distributor


class AdditionalProduct(models.Model):
    PRODUCT_TYPES = [
        ('water', 'Woda butelkowana'),
        ('coffee', 'Kawa'),
        ('tea', 'Herbata'),
    ]

    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.quantity})"


class Delivery(models.Model):
    delivery_date = models.DateField()
    driver = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE)
    full_bottles_delivered = models.PositiveIntegerField(default=0)
    empty_bottles_collected = models.PositiveIntegerField(default=0)
    distributors_delivered = models.ManyToManyField(Distributor, related_name='deliveries_delivered', blank=True)
    distributors_collected = models.ManyToManyField(Distributor, related_name='deliveries_collected', blank=True)
    additional_products = models.ManyToManyField(AdditionalProduct, blank=True)
    client_signature = models.FileField(upload_to='signatures/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Dostawa {self.delivery_date} - {self.delivery_address}"
