from django.contrib import admin
from .models import Distributor


@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'device_type', 'model', 'status', 'owner', 'client', 'delivery_address')
    search_fields = ('serial_number', 'barcode', 'device_type', 'model', 'client__name')
    list_filter = ('status', 'owner')
