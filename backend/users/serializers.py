from rest_framework import serializers
from .models import User
from clients.models import Client


class UserSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'client', 'is_active', 'is_staff']
