from rest_framework import viewsets
from .models import Delivery, AdditionalProduct
from .serializers import DeliverySerializer, AdditionalProductSerializer


class AdditionalProductViewSet(viewsets.ModelViewSet):
    queryset = AdditionalProduct.objects.all()
    serializer_class = AdditionalProductSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
