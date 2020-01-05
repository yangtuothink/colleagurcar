from django.db.models import Q
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from order.serializer import OrderSerializer, DriverSquareSerializer, CustomerSquareSerializer
from order.serializer import CancelLogSerializer, ChatMessageSerializer, CourseCommentsSerializer
from utils.permissioms import OrderHasUserOrReadOnly, UserIsDriver, UserIsCustomer
from .models import Order, DriverSquare, CustomerSquare, CancelLog, ChatMessage, CourseComments


# 分页
class CustomPagination(PageNumberPagination):
    # 默认每页显示的个数
    page_size = 10
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


# 订单视图
class OrderView(viewsets.ModelViewSet):
    """
    list:
    返回当前用户订单数据

    update:
    更新用户订单

    create:
    创建用户订单
    
    read:
    查看单条订单
    """
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
    filter_backends = (OrderingFilter,)
    permission_classes = (IsAuthenticated,)
    ordering_fields = ['add_time']
    
    def get_queryset(self):
        # 获得当前登录人的 订单
        return Order.objects.all().filter(Q(customer=self.request.user) | Q(driver__user_id=self.request.user))


# 司机行程广场
class DriverSquareView(viewsets.ModelViewSet):
    """
    list:
    返回司机行程广场数据

    update:
    更新司机行程广场数据

    create:
    创建司机行程广场数据

    read:
    查看单条司机行程广场数据

    delete:
    删除司机行程广场数据
    """
    queryset = DriverSquare.objects.filter(r_status=0)
    serializer_class = DriverSquareSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, UserIsDriver)
    ordering_fields = ['add_time']
    filterset_fields = ["label_type", "origin", "finish"]


# 乘客行程广场
class CustomerSquareView(viewsets.ModelViewSet):
    """
    list:
    返回乘客行程广场数据

    update:
    更新乘客行程广场数据

    create:
    创建乘客行程广场数据

    read:
    查看单条乘客行程广场数据

    delete:
    删除乘客行程广场数据
    """
    serializer_class = CustomerSquareSerializer
    queryset = CustomerSquare.objects.filter(r_status=0)
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, UserIsCustomer)
    ordering_fields = ['add_time']
    filterset_fields = ["label_type", "origin", "finish"]


# 取消订单日志
class CancelLogView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    """
    list:
    返回取消订单日志所有数据

    create:
    创建取消订单

    read:
    查看单条取消订单日志数据
    """
    serializer_class = CancelLogSerializer
    filter_backends = (OrderingFilter,)
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, OrderHasUserOrReadOnly)
    lookup_field = 'order_id'
    ordering_fields = ['add_time']
    
    def get_queryset(self):
        # 获得当前登录人的取消订单记录
        return CancelLog.objects.filter(
            Q(order__customer=self.request.user) | Q(order__driver__user_id=self.request.user))


# 订单聊天记录
class ChatMessageView(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    list:
    返回订单聊天记录所有数据

    create:
    创建订单聊天记录数据
    """
    serializer_class = ChatMessageSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, OrderHasUserOrReadOnly)
    ordering_fields = ['add_time']
    filterset_fields = ["order"]
    
    def get_queryset(self):
        # 获得当前登录人的订单聊天记录
        return ChatMessage.objects.filter(
            Q(order__customer=self.request.user) | Q(order__driver__user_id=self.request.user))


# 订单评论记录
class CourseCommentsView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    """
    list:
    返回订单评论记录所有数据

    create:
    创建订单评论记录数据

    read:
    查看订单评论记录数据
    """
    serializer_class = CourseCommentsSerializer
    filter_backends = (OrderingFilter,)
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, OrderHasUserOrReadOnly)
    lookup_field = 'order_id'
    ordering_fields = ['add_time']
    
    def get_queryset(self):
        # 获得当前登录人的评论记录
        return CourseComments.objects.filter(
            Q(order__customer=self.request.user) | Q(order__driver__user_id=self.request.user))
