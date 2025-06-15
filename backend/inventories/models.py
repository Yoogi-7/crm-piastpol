from django.db import models
from clients.models import Client, DeliveryAddress
from equipment.models import Distributor
from users.models import User


class Inventory(models.Model):
    inventory_date = models.DateField()
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE)
    bottle_quantity = models.PositiveIntegerField(default=0)
    distributors = models.ManyToManyField(Distributor, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Inwentaryzacja {self.inventory_date} - {self.client.name}"
