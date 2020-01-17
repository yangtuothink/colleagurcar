from datetime import datetime
from django.db import models

from examine.models import DriverProfile
from django.contrib.auth import get_user_model

User = get_user_model()


# 司机行程广场
class DriverOrder(models.Model):
    ORDER_STATUS = (
        (0, "已发布待预约"),
        (1, "已预约待出发"),
        (2, "行程中"),
        (3, "待支付"),
        (4, "已关闭"),
        (5, "已完成"),
    )
    initiator = models.ForeignKey(User, verbose_name="司机 id", on_delete=models.CASCADE, help_text="司机 id")
    origin = models.CharField(max_length=200, verbose_name="起点", default="", blank=True, help_text="起点")
    finish = models.CharField(max_length=200, verbose_name="终点", default="", blank=True, help_text="终点")
    remarks = models.CharField(max_length=200, verbose_name="备注", default="", blank=True, help_text="备注")
    mount = models.CharField(max_length=200, verbose_name="预测金额", default=30, blank=True, help_text="预测金额")
    p_num = models.CharField(max_length=200, verbose_name="乘坐人数", default=1, help_text="乘坐人数")
    r_status = models.CharField(choices=(("y", "已预订"), ("n", "待预定")), default="n", max_length=30, verbose_name="订单状态",
                                help_text="订单状态 y/n - 已预订/待预定")
    label_type = models.CharField(choices=(("m", "上班"), ("n", "下班")), default="m", max_length=30, verbose_name="出行类别",
                                  help_text="m/n - 上班/下班 出行类别")
    s_time = models.DateTimeField(default=datetime.now, verbose_name="出发起始时间", help_text="出发起始时间")
    e_time = models.DateTimeField(default=datetime.now, verbose_name="出发截止时间", help_text="出发截止时间")
    
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号", help_text="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号",
                                help_text="交易号")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间", help_text="支付时间")
    p_sum = models.CharField(max_length=200, verbose_name="剩余可乘坐人数", default=3, help_text="剩余可乘坐人数")
    pay_status = models.CharField(choices=ORDER_STATUS, default=0, max_length=30, verbose_name="订单状态",
                                  help_text="订单状态 0/1/2/3/4/5 - 已发布待预约/已预约待出发/行程中/待支付/已关闭/已完成")
    
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "司机行程广场"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return "{}-{}".format(self.initiator, self.order_sn)


# 顾客行程广场
class CustomerOrder(models.Model):
    ORDER_STATUS = (
        (0, "已发布待接单"),
        (1, "行程待开始"),
        (2, "行程中"),
        (3, "待支付"),
        (4, "已关闭"),
        (5, "已完成"),
    )
    
    m_order = models.ForeignKey(DriverOrder, verbose_name="主订单 id", on_delete=models.CASCADE, help_text="主订单 id",
                                null=True)
    initiator = models.ForeignKey(User, verbose_name="顾客 id", on_delete=models.CASCADE, help_text="顾客 id")
    origin = models.CharField(max_length=200, verbose_name="起点", default="", blank=True, help_text="起点")
    finish = models.CharField(max_length=200, verbose_name="终点", default="", blank=True, help_text="终点")
    remarks = models.CharField(max_length=200, verbose_name="备注", default="", blank=True, help_text="备注")
    mount = models.CharField(max_length=200, verbose_name="预测金额", default="", blank=True, help_text="预测金额")
    p_num = models.CharField(max_length=200, verbose_name="乘坐人数", default=1, help_text="乘坐人数")
    r_status = models.CharField(choices=(("n", "待预定"), ("y", "已预订")), default="n", max_length=30, verbose_name="订单状态",
                                help_text="订单状态 y/n - 已预订/待预订")
    label_type = models.CharField(choices=(("m", "上班"), ("n", "下班")), default="m", max_length=30, verbose_name="出行类别",
                                  help_text="出行类别  m/n - 上班/下班")
    s_time = models.DateTimeField(default=datetime.now, verbose_name="出发时间", help_text="出发时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")
    
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号", help_text="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号",
                                help_text="交易号")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间", help_text="支付时间")
    pay_status = models.CharField(choices=ORDER_STATUS, default=0, max_length=30, verbose_name="订单状态",
                                  help_text="订单状态 0/1/2/3/4/5 - 已发布待预约/行程待开始/行程中/待支付/已关闭/已完成")
    
    class Meta:
        verbose_name = "顾客行程广场"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return "{}-{}".format(self.initiator, self.order_sn)


# 订单聊天记录
class ChatMessage(models.Model):
    m_order = models.ForeignKey(DriverOrder, verbose_name="主订单 id", on_delete=models.CASCADE, help_text="主订单 id",
                                null=True)
    order = models.ForeignKey(CustomerOrder, verbose_name="子订单 id", on_delete=models.CASCADE, help_text="子订单 id")
    message = models.CharField(max_length=500, default="", verbose_name="信息内容", blank=True, help_text="信息内容")
    sender = models.CharField(max_length=30, choices=(("c", "乘客"), ("d", "司机")), default="c",
                              verbose_name="发送人角色 1/2 - 乘客/司机")
    has_read = models.CharField(max_length=30, choices=(("g", "好评"), ("b", "差评")), default="b", verbose_name="是否已读",
                                blank=True, help_text="是否已读 0/1 - 未/已")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "订单聊天记录"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return "{}-{}".format(self.order, self.message)


# 用户行程评价
class CourseComments(models.Model):
    order = models.ForeignKey(CustomerOrder, verbose_name="订单 id", on_delete=models.CASCADE, help_text="订单 id",
                              unique=True)
    star = models.IntegerField(default=0, verbose_name="星级", blank=True, help_text="星级 1-5")
    submitter = models.CharField(max_length=30, choices=(("c", "乘客"), ("d", "司机")), default="c",
                                 verbose_name="提交评论角色  c/g - 乘客/司机")
    c_label = models.CharField(max_length=30, choices=(("g", "好评"), ("b", "差评")), default="b", verbose_name="评论类别",
                               help_text="评论类别 g:好评, b:差评 默认 好评")
    comments = models.CharField(max_length=200, default="", verbose_name="评论内容", blank=True, help_text="评论内容")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "行程评价"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.order


# 异常取消订单
class CancelLog(models.Model):
    m_order = models.ForeignKey(DriverOrder, verbose_name="订单", on_delete=models.CASCADE, help_text="订单 id",
                                null=True)
    order = models.ForeignKey(CustomerOrder, verbose_name="订单", on_delete=models.CASCADE, help_text="订单 id",
                              unique=True)
    cancel = models.CharField(max_length=50, choices=(("c", "顾客"), ("d", "司机")), help_text="取消人角色  c/d - 顾客/司机")
    punish = models.CharField(max_length=50, blank=True, default="", help_text="取消备注留言")
    overtime = models.CharField(max_length=50, verbose_name="下单后时长", default="00:02", blank=True,
                                help_text="下单后时长, 格式: 00:20 ")
    deduction = models.CharField(max_length=50, verbose_name="扣分值", default=5, blank=True, help_text="扣分值")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "行程订单"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.order
