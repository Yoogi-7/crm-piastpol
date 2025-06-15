from rest_framework import viewsets
from .models import Client, DeliveryAddress
from .serializers import ClientSerializer, DeliveryAddressSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DeliveryAddressViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer
