from django.contrib import admin
from .models import Delivery, AdditionalProduct


@admin.register(AdditionalProduct)
class AdditionalProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'quantity')
    list_filter = ('product_type',)
    search_fields = ('name',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('delivery_date', 'driver', 'delivery_address')
    list_filter = ('delivery_date',)
    search_fields = ('delivery_address__location_name', 'driver__username')
