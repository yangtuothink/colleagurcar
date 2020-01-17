from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户表 - 继承
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="阿一", help_text="昵称")
    birday = models.DateField(verbose_name="生日", null=True, help_text="生日", default=datetime.now)
    gender = models.CharField(max_length=6, verbose_name="性别", choices=(("male", "男"), ("female", "女")), default="male",
                              help_text="性别  male/female - 男/女")
    address = models.CharField(max_length=100, default="", blank=True, help_text="地址")
    mobile = models.CharField(max_length=11, default="15681234566", help_text="电话")
    image = models.ImageField(max_length=100, verbose_name="头像", upload_to="users/images/%Y%m%d",
                              default="users/images/default.png", help_text="头像")
    home = models.CharField(max_length=100, verbose_name="家地址", default="", blank=True, help_text="家地址")
    company_address = models.CharField(max_length=100, verbose_name="公司地址", default="", blank=True, help_text="公司地址")
    company = models.CharField(max_length=100, verbose_name="公司名称", default="", blank=True, help_text="公司名称")
    department = models.CharField(max_length=100, verbose_name="部门", default="", blank=True, help_text="部门")
    credit_score = models.IntegerField(default=100, verbose_name="信用积分", help_text="信用积分")
    money = models.CharField(max_length=100, verbose_name="余额", default=0, help_text="余额")
    is_driver = models.CharField(max_length=100, choices=(("n", "否"), ("y", "是")), verbose_name="是否司机", default="n",
                                 help_text="是否司机")
    
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.username


# 银行卡绑定
class BankCard(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="用户 id", help_text="用户 id")
    card_num = models.CharField(max_length=200, verbose_name="卡号", help_text="卡号")
    bank = models.URLField(max_length=200, verbose_name="所属银行", blank=True, null=True, help_text="所属银行")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "银行卡绑定"
        verbose_name_plural = verbose_name


# 系统信息推送顾客
class CustomerMessage(models.Model):
    receiver = models.ForeignKey(UserProfile, verbose_name="接收人", on_delete=models.CASCADE, help_text="接收人 - 顾客 id")
    message = models.CharField(max_length=500, verbose_name="信息内容", default="", blank=True, help_text="信息内容")
    has_read = models.CharField(max_length=30, default="未读", choices=(("y", "已读"), ("n", "未读")), verbose_name="n",
                                blank=True, help_text="是否已读 0/1 - 未/已")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "系统信息推送顾客"
        verbose_name_plural = verbose_name


# 首页广告轮播
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题", null=True, help_text="标题")
    image = models.ImageField(max_length=200, upload_to="users/images/%Y%m%d", verbose_name="轮播图", help_text="轮播图")
    url = models.URLField(max_length=200, verbose_name="访问地址", blank=True, null=True, help_text="访问地址")
    index = models.IntegerField(default=1, verbose_name="顺序", help_text="顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
