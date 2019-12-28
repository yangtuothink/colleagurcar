from rest_framework import viewsets

from order.serializer import OrderSerializer, DriverSquareSerializer, CustomerSquareSerializer
from .models import Order, DriverSquare, CustomerSquare


class OrderView(viewsets.ModelViewSet):
    """
    list:
    返回当前用户订单数据

    update:
    更新用户订单

    create:
    创建用户订单

    delete:
    删除订单
    """
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)


class DriverSquareView(viewsets.ModelViewSet):
    queryset = DriverSquare.objects.all()
    serializer_class = DriverSquareSerializer


class CustomerSquareView(viewsets.ModelViewSet):
    queryset = CustomerSquare.objects.all()
    serializer_class = CustomerSquareSerializer
