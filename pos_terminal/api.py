from .models import Orders
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
  queryset = Orders.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = OrderSerializer