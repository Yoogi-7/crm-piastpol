from django.contrib.auth.models import AbstractUser
from django.db import models
from clients.models import Client


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('office', 'Biuro'),
        ('driver', 'Kierowca'),
        ('client', 'Klient'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='office')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
