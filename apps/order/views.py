from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from order.serializer import OrderSerializer, DriverSquareSerializer, CustomerSquareSerializer, CancelLogSerializer, \
    ChatMessageSerializer, CourseCommentsSerializer
from .models import Order, DriverSquare, CustomerSquare, CancelLog, ChatMessage, CourseComments


class OrderPagination(PageNumberPagination):
    """
    商品列表自定义分页
    """
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

    delete:
    删除订单
    """
    serializer_class = OrderSerializer
    pagination_class = OrderPagination
    ordering_fields = ('add_time')
    
    def get_queryset(self):
        # 获得当前登录人的 订单
        return Order.objects.all().filter(customer=self.request.user)


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
    queryset = DriverSquare.objects.all()
    serializer_class = DriverSquareSerializer


# 乘客行程广场
class CustomerSquareView(viewsets.ModelViewSet):
    queryset = CustomerSquare.objects.all()
    serializer_class = CustomerSquareSerializer


# 取消订单日志
class CancelLogView(GenericViewSet, mixins.ListModelMixin):
    queryset = CancelLog.objects.all()
    serializer_class = CancelLogSerializer
    
    def get_queryset(self):
        # 获得当前登录人的取消订单记录
        return CancelLog.objects.filter(order__customer=self.request.user).order_by()


# 订单聊天记录
class ChatMessageView(GenericViewSet, mixins.ListModelMixin):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
    
    def get_queryset(self):
        # 获得当前登录人的订单聊天记录
        return ChatMessage.objects.filter(order__customer=self.request.user)


# 订单评论记录
class CourseCommentsView(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CourseCommentsSerializer
    
    def get_queryset(self):
        # 获得当前登录人的评论记录
        return CourseComments.objects.filter(order__customer=self.request.user)
