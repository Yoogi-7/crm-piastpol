from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer
from clients.models import Client
from clients.serializers import ClientSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def profile(self, request):
        user = request.user
        data = UserSerializer(user).data
        if user.role == 'client' and user.client:
            client_data = ClientSerializer(user.client).data
            data['client_info'] = client_data
        return Response(data)
