from rest_framework import viewsets, permissions
from .models import Delivery, AdditionalProduct
from .serializers import DeliverySerializer, AdditionalProductSerializer
from users.models import User

class AdditionalProductViewSet(viewsets.ModelViewSet):
    queryset = AdditionalProduct.objects.all()
    serializer_class = AdditionalProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'client' and user.client:
            return Delivery.objects.filter(client=user.client)
        return Delivery.objects.all()
