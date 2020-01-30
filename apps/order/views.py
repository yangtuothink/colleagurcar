from rest_framework import viewsets, mixins, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from order.filters import DriverOrderFilter, CustomerOrderFilter
from order.serializer import DriverOrderSerializer, CustomerOrderSerializer
from order.serializer import CancelLogSerializer, ChatMessageSerializer, CourseCommentsSerializer
from utils.permissioms import IsOrderCustomer, IsOrderDriver, CommentsReadOnly
from .models import DriverOrder, CustomerOrder, CancelLog, ChatMessage, CourseComments


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


# 司机订单视图
class DriverOrderView(viewsets.ModelViewSet):
    """
    list:
    返回当前用户司机订单数据

    update:
    更新用户司机订单

    create:
    创建用户司机订单
    
    read:
    查看单条司机订单
    """
    serializer_class = DriverOrderSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = DriverOrderFilter
    permission_classes = (IsAuthenticated, IsOrderDriver)
    ordering_fields = ['add_time', ]
    search_fields = ["origin", "finish"]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.perform_create(serializer)
        re_dict = serializer.data if order else "无权操作"
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        if self.request.user.is_driver == "y":
            return serializer.save()
    
    def get_queryset(self):
        # 司机状态只能查看自己的订单
        if self.request.user.is_driver == "y":
            return DriverOrder.objects.all().filter(initiator=self.request.user).order_by('-add_time')
        # 乘客看到所有待预定的订单
        return DriverOrder.objects.filter(r_status="y").order_by('-add_time')


# 用户订单视图
class CustomerOrderView(viewsets.ModelViewSet):
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
    serializer_class = CustomerOrderSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    permission_classes = (IsAuthenticated, IsOrderCustomer)
    filterset_class = CustomerOrderFilter
    ordering_fields = ['add_time']
    filterset_fields = ["label_type"]
    search_fields = ("origin", "finish")
    
    def get_queryset(self):
        # 乘客只能查看自己的订单
        if self.request.user.is_driver == "n":
            return CustomerOrder.objects.all().filter(initiator=self.request.user).order_by('-add_time')
        # 司机看到所有可预约的订单
        return CustomerOrder.objects.filter(r_status="y").order_by('-add_time')
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = self.perform_create(serializer)
        re_dict = serializer.data if order else "无权操作"
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        if self.request.user.is_driver == "n":
            return serializer.save()


# 订单聊天记录
class ChatMessageView(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    list:
    返回订单聊天记录所有数据

    create:
    创建订单聊天记录数据
    """
    queryset = ChatMessage.objects.all().order_by('-add_time')
    serializer_class = ChatMessageSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)
    ordering_fields = ['add_time']
    filterset_fields = ["order"]


# 订单评论记录
class CourseCommentsView(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    """
    list:
    返回订单评论记录所有数据

    create:
    创建订单评论记录数据

    read:
    查看订单评论记录数据 查找索引为 子订单 id
    """
    serializer_class = CourseCommentsSerializer
    filter_backends = (OrderingFilter,)
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated, CommentsReadOnly)
    ordering_fields = ['add_time']
    lookup_field = 'order'
    filterset_fields = ["order"]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        re_dict = serializer.data if self.perform_create(serializer) else "无权操作"
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        if self.request.user.is_driver == "n" and CustomerOrder.objects.filter(initiator=self.request.user,
                                                                               id=self.request.data["order"]):
            return serializer.save()
    
    def get_queryset(self):
        return CourseComments.objects.filter(order__initiator=self.request.user).order_by('-add_time')


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
    permission_classes = (IsAuthenticated,)
    ordering_fields = ['add_time']
    
    def get_queryset(self):
        # 获得当前登录人的取消订单记录
        return CancelLog.objects.filter(submitter=self.request.user).order_by("-add_time")
