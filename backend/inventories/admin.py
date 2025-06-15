from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_date', 'client', 'delivery_address', 'driver', 'bottle_quantity')
    list_filter = ('inventory_date',)
    search_fields = ('client__name', 'delivery_address__location_name', 'driver__username')
