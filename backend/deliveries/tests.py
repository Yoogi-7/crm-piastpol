from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from clients.models import Client, DeliveryAddress
from deliveries.models import Delivery

User = get_user_model()

class DeliveriesTests(APITestCase):

    def setUp(self):
        self.client_data = Client.objects.create(
            name="Test Client",
            nip="1234567890",
            email="client@example.com",
            phone="123456789"
        )

        self.address = DeliveryAddress.objects.create(
            client=self.client_data,
            location_name="Main Office",
            street="Main St",
            city="City",
            province="Province",
            postal_code="00-000"
        )

        self.user = User.objects.create_user(
            username="clientuser",
            password="clientpass",
            role="client",
            client=self.client_data
        )

        self.delivery = Delivery.objects.create(
            client=self.client_data,
            delivery_address=self.address,
            delivery_date="2025-06-15",
            driver=self.user
        )

    def authenticate(self):
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {'username': 'clientuser', 'password': 'clientpass'})
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_client_deliveries(self):
        self.authenticate()
        response = self.client.get(reverse('delivery-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['delivery_date'], "2025-06-15")
