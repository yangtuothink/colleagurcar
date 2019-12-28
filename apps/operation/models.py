# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from examine.models import DriverProfile, FoulRule
from order.models import Order

User = get_user_model()


# 系统信息推送顾客
class CustomerMessage(models.Model):
    receiver = models.ForeignKey(User, verbose_name="接收人", on_delete=models.CASCADE)
    message = models.CharField(max_length=500, verbose_name="信息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "系统信息推送顾客"
        verbose_name_plural = verbose_name


# 系统信息推送司机
class DriverMessage(models.Model):
    receiver = models.ForeignKey(DriverProfile, verbose_name="接收人", on_delete=models.CASCADE)
    message = models.CharField(max_length=500, verbose_name="信息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "系统信息推送司机"
        verbose_name_plural = verbose_name


# 订单聊天记录
class ChatMessage(models.Model):
    order = models.ForeignKey(Order, verbose_name="订单", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, verbose_name="发送人", on_delete=models.CASCADE)
    message = models.CharField(max_length=500, verbose_name="信息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


# 行程评价
class CourseComments(models.Model):
    customer = models.ForeignKey(User, verbose_name="顾客", on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverProfile, verbose_name="司机", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name="订单", on_delete=models.CASCADE)
    star = models.IntegerField(default=0, verbose_name="星级")
    c_label = models.CharField(max_length=200, choices=((1, "好评"), (2, "差评")), default=1, verbose_name="评论类别")
    comments = models.CharField(max_length=200, verbose_name="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "行程评价"
        verbose_name_plural = verbose_name


# 司机违规记录
class FoulLog(models.Model):
    applicant = models.ForeignKey(DriverProfile, verbose_name="违规人", on_delete=models.CASCADE)
    foul_rule = models.ForeignKey(FoulRule, verbose_name="违规条目", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "违规记录"
        verbose_name_plural = verbose_name


# 异常取消订单
class CancelLog(models.Model):
    customer = models.ForeignKey(User, verbose_name="顾客", on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverProfile, verbose_name="司机", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name="订单", on_delete=models.CASCADE)
    cancel = models.CharField(max_length=50, choices=((1, "顾客"), (2, "司机")))
    punish = models.CharField(max_length=50)
    overtime = models.CharField(max_length=50, verbose_name="超时时长")
    deduction = models.CharField(max_length=50, verbose_name="扣分")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "行程订单"
        verbose_name_plural = verbose_name
