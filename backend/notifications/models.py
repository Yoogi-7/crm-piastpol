from django.db import models


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('reminder', 'Przypomnienie o dostawie'),
        ('confirmation', 'Potwierdzenie dostawy'),
        ('block', 'Wstrzymanie dostawy'),
    ]

    type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    content = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    send_time = models.DateTimeField(auto_now_add=True)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} - {self.send_time}"
