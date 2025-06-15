from rest_framework import serializers
from .models import Client, DeliveryAddress


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    addresses = DeliveryAddressSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'
