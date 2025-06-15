from rest_framework import serializers
from .models import Delivery, AdditionalProduct
from equipment.serializers import DistributorSerializer
from clients.serializers import DeliveryAddressSerializer
from users.models import User
from clients.models import Client


class AdditionalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalProduct
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    distributors_delivered = DistributorSerializer(many=True, read_only=True)
    distributors_collected = DistributorSerializer(many=True, read_only=True)
    delivery_address = DeliveryAddressSerializer(read_only=True)
    additional_products = AdditionalProductSerializer(many=True, read_only=True)
    driver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Delivery
        fields = '__all__'
