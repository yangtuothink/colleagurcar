# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Order, DriverSquare, CustomerSquare, CourseComments, ChatMessage, CancelLog


class OrderSerializer(serializers.ModelSerializer):
    # 订单的某些信息是不能自己修改的
    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    customer = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    # 生成订单号函数
    def generate_order_sn(self):
        # 当前时间+userid+随机数
        from time import strftime
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id,
                                                       ranstr=random_ins.randint(10, 99))
        return order_sn
    
    # 对订单号进行生成
    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs
    
    class Meta:
        model = Order
        fields = "__all__"


class DriverSquareSerializer(serializers.ModelSerializer):
    initiator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = DriverSquare
        fields = "__all__"


class CustomerSquareSerializer(serializers.ModelSerializer):
    initiator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = CustomerSquare
        fields = "__all__"


class CourseCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseComments
        fields = "__all__"


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"


class CancelLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CancelLog
        fields = "__all__"
