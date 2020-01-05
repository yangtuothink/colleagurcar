from datetime import datetime
from django.db import models

from examine.models import DriverProfile
from django.contrib.auth import get_user_model

User = get_user_model()


# 行程订单
class Order(models.Model):
    ORDER_STATUS = (
        (0, "待进行"),
        (1, "正在进行"),
        (2, "待支付"),
        (3, "交易创建"),
        (4, "交易结束"),
        (5, "超时关闭"),
    )
    customer = models.ForeignKey(User, verbose_name="顾客 id", on_delete=models.CASCADE, help_text="顾客 id")
    driver = models.ForeignKey(DriverProfile, verbose_name="司机 id", on_delete=models.CASCADE, help_text="司机 id")
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号", help_text="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号",
                                help_text="交易号")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间", help_text="支付时间")
    mileage = models.CharField(max_length=200, verbose_name="里程", default="", help_text="里程", blank=True)
    origin = models.CharField(max_length=200, verbose_name="起点", default="", help_text="起点", blank=True)
    finish = models.CharField(max_length=200, verbose_name="终点", default="", help_text="终点", blank=True)
    take_time = models.CharField(max_length=200, verbose_name="耗时", default="", help_text="耗时", blank=True)
    amount = models.CharField(max_length=200, verbose_name="金额", default="", help_text="金额", blank=True)
    p_num = models.CharField(max_length=200, verbose_name="乘坐人数", default=1, help_text="乘坐人数")
    s_time = models.DateTimeField(null=True, verbose_name="出发时间", help_text="出发时间", blank=True)
    e_time = models.DateTimeField(null=True, verbose_name="抵达时间", help_text="抵达时间", blank=True)
    pay_status = models.CharField(choices=ORDER_STATUS, default=0, max_length=30, verbose_name="订单状态",
                                  help_text="订单状态 0/1/2/3/4/5 - 待进行/正在进行/待支付/交易创建/交易结束/超时关闭")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")
    
    class Meta:
        verbose_name = "行程订单"
        verbose_name_plural = verbose_name


# 订单聊天记录
class ChatMessage(models.Model):
    order = models.ForeignKey(Order, verbose_name="订单 id", on_delete=models.CASCADE, help_text="订单 id")
    message = models.CharField(max_length=500, default="", verbose_name="信息内容", blank=True, help_text="信息内容")
    sender = models.CharField(max_length=30, choices=((1, "乘客"), (2, "司机")), default=1,
                              verbose_name="发送人角色 1/2 - 乘客/司机")
    has_read = models.CharField(max_length=30, default=0, choices=((1, "已读"), (0, "未读")), verbose_name="是否已读",
                                blank=True, help_text="是否已读 0/1 - 未/已")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "订单聊天记录"
        verbose_name_plural = verbose_name


# 用户行程评价
class CourseComments(models.Model):
    order = models.ForeignKey(Order, verbose_name="订单 id", on_delete=models.CASCADE, help_text="订单 id", unique=True)
    star = models.IntegerField(default=0, verbose_name="星级", blank=True, help_text="星级 1-5")
    submitter = models.CharField(max_length=30, choices=((1, "乘客"), (2, "司机")), default=1,
                                 verbose_name="提交评论角色  1/2 - 乘客/司机")
    c_label = models.CharField(max_length=30, choices=((1, "好评"), (2, "差评")), default=1, verbose_name="评论类别",
                               help_text="评论类别 1:好评, 2:差评 默认 好评")
    comments = models.CharField(max_length=200, default="", verbose_name="评论内容", blank=True, help_text="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "行程评价"
        verbose_name_plural = verbose_name


# 异常取消订单
class CancelLog(models.Model):
    order = models.ForeignKey(Order, verbose_name="订单", on_delete=models.CASCADE, help_text="订单 id", unique=True)
    cancel = models.CharField(max_length=50, choices=((1, "顾客"), (2, "司机")), help_text="取消人角色  1/2 - 顾客/司机")
    punish = models.CharField(max_length=50, blank=True, default="", help_text="取消备注留言")
    overtime = models.CharField(max_length=50, verbose_name="下单后时长", default="00:02", blank=True,
                                help_text="下单后时长, 格式: 00:20 ")
    deduction = models.CharField(max_length=50, verbose_name="扣分值", default=5, blank=True, help_text="扣分值")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "行程订单"
        verbose_name_plural = verbose_name


# 司机行程广场
class DriverSquare(models.Model):
    initiator = models.ForeignKey(DriverProfile, verbose_name="司机", on_delete=models.CASCADE, help_text="司机 id")
    origin = models.CharField(max_length=200, verbose_name="起点", default="", blank=True, help_text="起点")
    finish = models.CharField(max_length=200, verbose_name="终点", default="", blank=True, help_text="终点")
    remarks = models.CharField(max_length=200, verbose_name="备注", default="", blank=True, help_text="备注")
    mount = models.CharField(max_length=200, verbose_name="预测金额", default=30, blank=True, help_text="预测金额")
    p_num = models.CharField(max_length=200, verbose_name="乘坐人数", default=1, help_text="乘坐人数")
    r_status = models.CharField(choices=((1, "已预订"), (0, "待预定")), default=0, max_length=30, verbose_name="订单状态",
                                help_text="订单状态")
    label_type = models.CharField(choices=((1, "上班"), (2, "下班"),), default=1, max_length=30, verbose_name="出行类别",
                                  help_text="出行类别")
    s_time = models.DateTimeField(verbose_name="出发起始时间", help_text="出发起始时间")
    e_time = models.DateTimeField(verbose_name="出发截止时间", help_text="出发截止时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "司机行程广场"
        verbose_name_plural = verbose_name


# 顾客行程广场
class CustomerSquare(models.Model):
    initiator = models.ForeignKey(User, verbose_name="顾客 id", on_delete=models.CASCADE, help_text="顾客 id")
    origin = models.CharField(max_length=200, verbose_name="起点", default="", blank=True, help_text="起点")
    finish = models.CharField(max_length=200, verbose_name="终点", default="", blank=True, help_text="终点")
    remarks = models.CharField(max_length=200, verbose_name="备注", default="", blank=True, help_text="备注")
    mount = models.CharField(max_length=200, verbose_name="预测金额", default="", blank=True, help_text="预测金额")
    p_num = models.CharField(max_length=200, verbose_name="乘坐人数", default=1, help_text="乘坐人数")
    r_status = models.CharField(choices=((1, "已预订"), (0, "待预定")), default=0, max_length=30, verbose_name="订单状态",
                                help_text="订单状态")
    label_type = models.CharField(choices=((1, "上班"), (2, "下班"),), default=1, max_length=30, verbose_name="出行类别",
                                  help_text="出行类别")
    s_time = models.DateTimeField(verbose_name="出发时间", help_text="出发时间")
    add_time = models.DateTimeField(verbose_name="添加时间", help_text="添加时间")
    
    class Meta:
        verbose_name = "顾客行程广场"
        verbose_name_plural = verbose_name
