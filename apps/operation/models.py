# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from examine.models import DriverProfile, FoulRule
from order.models import Order

User = get_user_model()


# 系统信息推送顾客
class CustomerMessage(models.Model):
    receiver = models.ForeignKey(User, verbose_name="接收人", on_delete=models.CASCADE, help_text="接收人 - 顾客 id")
    message = models.CharField(max_length=500, verbose_name="信息内容", default="", blank=True, help_text="信息内容")
    has_read = models.CharField(max_length=30, default="未读", choices=((1, "已读"), (0, "未读")), verbose_name="是否已读",
                                blank=True, help_text="是否已读 0/1 - 未/已")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "系统信息推送顾客"
        verbose_name_plural = verbose_name


# 系统信息推送司机
class DriverMessage(models.Model):
    receiver = models.ForeignKey(DriverProfile, verbose_name="接收人", on_delete=models.CASCADE, help_text="接收人 司机 id")
    message = models.CharField(max_length=500, verbose_name="信息内容", default="", blank=True, help_text="信息内容")
    has_read = models.CharField(max_length=30, default="未读", choices=((1, "已读"), (0, "未读")), verbose_name="是否已读",
                                blank=True, help_text="是否已读 0/1 - 未/已")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "系统信息推送司机"
        verbose_name_plural = verbose_name


# 订单聊天记录
class ChatMessage(models.Model):
    order = models.ForeignKey(Order, verbose_name="订单 id", on_delete=models.CASCADE, help_text="订单 id")
    customer = models.ForeignKey(User, verbose_name="顾客 id", on_delete=models.CASCADE, help_text="顾客 id")
    driver = models.ForeignKey(DriverProfile, verbose_name="司机 id", on_delete=models.CASCADE, help_text="司机 id")
    message = models.CharField(max_length=500, default="", verbose_name="信息内容", blank=True, help_text="信息内容")
    has_read = models.CharField(max_length=30, default="未读", choices=((1, "已读"), (0, "未读")), verbose_name="是否已读",
                                blank=True, help_text="是否已读 0/1 - 未/已")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


# 行程评价
class CourseComments(models.Model):
    customer = models.ForeignKey(User, verbose_name="顾客 id", on_delete=models.CASCADE, help_text="顾客 id")
    driver = models.ForeignKey(DriverProfile, verbose_name="司机 id", on_delete=models.CASCADE, help_text="司机 id")
    order = models.ForeignKey(Order, verbose_name="订单 id", on_delete=models.CASCADE, help_text="订单 id")
    star = models.IntegerField(default=0, verbose_name="星级", blank=True, help_text="星级 1-5")
    c_label = models.CharField(max_length=30, choices=((1, "好评"), (2, "差评")), default="好评", verbose_name="评论类别",
                               help_text="评论类别 1:好评, 2:差评 默认 好评")
    comments = models.CharField(max_length=200, default="", verbose_name="评论内容", blank=True, help_text="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "行程评价"
        verbose_name_plural = verbose_name


# 司机违规记录
class FoulLog(models.Model):
    applicant = models.ForeignKey(DriverProfile, verbose_name="违规人 - 司机 id", on_delete=models.CASCADE,
                                  help_text="违规人 -  司机 id")
    foul_rule = models.ForeignKey(FoulRule, verbose_name="违规条目 id", on_delete=models.CASCADE, help_text="违规条目 id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "违规记录"
        verbose_name_plural = verbose_name


# 异常取消订单
class CancelLog(models.Model):
    customer = models.ForeignKey(User, verbose_name="顾客", on_delete=models.CASCADE, help_text="顾客 id")
    driver = models.ForeignKey(DriverProfile, verbose_name="司机", on_delete=models.CASCADE, help_text="司机 id")
    order = models.ForeignKey(Order, verbose_name="订单", on_delete=models.CASCADE, help_text="订单 id")
    cancel = models.CharField(max_length=50, choices=((1, "顾客"), (2, "司机")), help_text="取消者  1/2 - 顾客/司机")
    punish = models.CharField(max_length=50, blank=True, default="", help_text="取消备注留言")
    overtime = models.CharField(max_length=50, verbose_name="下单后时长", default="00:02", blank=True,
                                help_text="下单后时长, 格式: 00:20 ")
    deduction = models.CharField(max_length=50, verbose_name="扣分值", default=5, blank=True, help_text="扣分值")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "行程订单"
        verbose_name_plural = verbose_name
