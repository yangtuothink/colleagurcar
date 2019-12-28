from datetime import datetime
from django.db import models

from examine.models import DriverProfile
from django.contrib.auth import get_user_model

User = get_user_model()


# 行程订单
class Order(models.Model):
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("paying", "待支付"),
    )
    customer = models.ForeignKey(User, verbose_name="顾客", on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverProfile, verbose_name="司机", on_delete=models.CASCADE)
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    mileage = models.CharField(max_length=200, verbose_name="里程", default="")
    origin = models.CharField(max_length=200, verbose_name="起点", default="")
    finish = models.CharField(max_length=200, verbose_name="终点", default="")
    take_time = models.CharField(max_length=200, verbose_name="耗时", default="")
    amount = models.CharField(max_length=200, verbose_name="金额", default="")
    p_num = models.CharField(max_length=200, verbose_name="乘坐人数", default=1)
    s_time = models.DateTimeField(default=datetime.now, verbose_name="出发时间")
    e_time = models.DateTimeField(default=datetime.now, verbose_name="抵达时间")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="订单状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "行程订单"
        verbose_name_plural = verbose_name


# 司机行程广场
class DriverSquare(models.Model):
    RESERVE_STATUS = (
        ("RESERVED", "已预订"),
        ("RESERVING", "待预定"),
    )
    initiator = models.ForeignKey(DriverProfile, verbose_name="司机", on_delete=models.CASCADE)
    origin = models.CharField(max_length=200, verbose_name="起点", default="")
    finish = models.CharField(max_length=200, verbose_name="终点", default="")
    remarks = models.CharField(max_length=200, verbose_name="备注", default="")
    mount = models.CharField(max_length=200, verbose_name="预测金额", default="")
    p_num = models.CharField(max_length=200, verbose_name="乘坐人数", default=1)
    r_status = models.CharField(choices=RESERVE_STATUS, default="RESERVING", max_length=30, verbose_name="订单状态")
    label_type = models.CharField(choices=((1, "上班"), (2, "下班"),), default=1, max_length=30, verbose_name="出行类别")
    s_time = models.DateTimeField(default=datetime.now, verbose_name="出发起始时间")
    e_time = models.DateTimeField(default=datetime.now, verbose_name="出发截止时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


# 顾客行程广场
class CustomerSquare(models.Model):
    RESERVE_STATUS = (
        ("RESERVED", "已预订"),
        ("RESERVING", "待预定"),
    )
    
    initiator = models.ForeignKey(User, verbose_name="顾客", on_delete=models.CASCADE)
    origin = models.CharField(max_length=200, verbose_name="起点", default="")
    finish = models.CharField(max_length=200, verbose_name="终点", default="")
    remarks = models.CharField(max_length=200, verbose_name="备注", default="")
    mount = models.CharField(max_length=200, verbose_name="预测金额", default="")
    p_num = models.CharField(max_length=200, verbose_name="乘坐人数", default=1)
    r_status = models.CharField(choices=RESERVE_STATUS, default="RESERVING", max_length=30, verbose_name="预定状态")
    label_type = models.CharField(choices=((1, "上班"), (2, "下班"),), default=1, max_length=30, verbose_name="出行类别")
    s_time = models.DateTimeField(default=datetime.now, verbose_name="出发时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
