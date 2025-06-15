from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    nip = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    delivery_blocked = models.BooleanField(default=False)
    block_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class DeliveryAddress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='addresses')
    location_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.location_name} ({self.client.name})"
