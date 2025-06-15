from rest_framework import serializers
from .models import Inventory
from equipment.serializers import DistributorSerializer
from clients.serializers import DeliveryAddressSerializer
from users.models import User
from clients.models import Client


class InventorySerializer(serializers.ModelSerializer):
    distributors = DistributorSerializer(many=True, read_only=True)
    delivery_address = DeliveryAddressSerializer(read_only=True)
    driver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Inventory
        fields = '__all__'
