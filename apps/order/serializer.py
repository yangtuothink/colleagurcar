# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import DriverOrder, CustomerOrder, CourseComments, ChatMessage, CancelLog
from examine.models import DriverProfile
from users.models import UserProfile


class DriverOrderSerializer(serializers.ModelSerializer):
    # 订单的某些信息是不能自己修改的
    # pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    initiator = serializers.HiddenField(
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
        model = DriverOrder
        fields = "__all__"


class CustomerOrderSerializer(serializers.ModelSerializer):
    # 订单的某些信息是不能自己修改的
    # pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    initiator = serializers.HiddenField(
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
        model = CustomerOrder
        fields = "__all__"


class CourseCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComments
        fields = "__all__"


class ChatMessageSerializer(serializers.ModelSerializer):
    initiator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = ChatMessage
        fields = "__all__"


class CancelLogSerializer(serializers.ModelSerializer):
    submitter = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    deduction = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        submitter = self.context["request"].user
        m_order = validated_data["m_order"]
        order = validated_data["order"]
        is_driver = validated_data["is_driver"]
        deduction = 5
        
        if is_driver == "y":
            # 主订单状态更新
            m_order.pay_status = "6"
            m_order.save()
            # 主订单扣分
            d_obj = DriverProfile.objects.get(user_id=submitter.id)
            d_obj.driver_score = d_obj.driver_score - 5 if d_obj.driver_score >= 5 else 0
            # 主订单下所有子订单更新
            for i in CustomerOrder.objects.filter(m_order=m_order.id):
                # 子订单司机扣分
                if int(i.pay_status) == 1:
                    d_obj.driver_score = d_obj.driver_score - 3 if d_obj.driver_score >= 3 else 0
                    deduction += 3
                if int(i.pay_status) == 2:
                    d_obj.driver_score = d_obj.driver_score - 5 if d_obj.driver_score >= 5 else 0
                    deduction += 5
                i.pay_status = "6"
                i.save()
            d_obj.save()
        else:
            # 子订单状态更新
            if int(order.pay_status) == 1:
                # 乘客扣分
                submitter.credit_score = submitter.credit_score - 5 if submitter.credit_score >= 5 else 0
                submitter.save()
            order.pay_status = "6"
            order.save()
        
        validated_data["deduction"] = deduction
        return CancelLog.objects.create(**validated_data)
    
    class Meta:
        model = CancelLog
        fields = "__all__"
