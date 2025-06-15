from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from clients.views import ClientViewSet, DeliveryAddressViewSet
from equipment.views import DistributorViewSet
from deliveries.views import DeliveryViewSet, AdditionalProductViewSet
from inventories.views import InventoryViewSet
from notifications.views import NotificationViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'addresses', DeliveryAddressViewSet)
router.register(r'distributors', DistributorViewSet)
router.register(r'deliveries', DeliveryViewSet)
router.register(r'additional-products', AdditionalProductViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
