from django.contrib import admin
from .models import Client, DeliveryAddress


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'nip', 'email', 'phone', 'delivery_blocked')
    search_fields = ('name', 'nip', 'email', 'phone')
    list_filter = ('delivery_blocked',)


@admin.register(DeliveryAddress)
class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'client', 'city', 'province')
    search_fields = ('location_name', 'client__name', 'city', 'province')
