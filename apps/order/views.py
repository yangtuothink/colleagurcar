from rest_framework import viewsets

from order.serializer import OrderSerializer
from .models import Order


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
