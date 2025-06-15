from rest_framework import viewsets
from .models import Distributor
from .serializers import DistributorSerializer


class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
