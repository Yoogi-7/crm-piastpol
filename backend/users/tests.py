from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from clients.models import Client

User = get_user_model()

class UserProfileTests(APITestCase):

    def setUp(self):
        self.client_data = Client.objects.create(
            name="Test Client",
            nip="1234567890",
            email="client@example.com",
            phone="123456789"
        )
        self.user = User.objects.create_user(
            username="clientuser",
            password="clientpass",
            role="client",
            client=self.client_data
        )

    def authenticate(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'clientuser', 'password': 'clientpass'})
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_login_and_profile(self):
        self.authenticate()

        response = self.client.get(reverse('user-profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'clientuser')
        self.assertEqual(response.data['client_info']['name'], 'Test Client')
