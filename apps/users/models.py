from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户表 - 继承
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birday = models.DateField(verbose_name="生日", null=True)
    gender = models.CharField(max_length=6, choices=(("", "男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, default="")
    image = models.ImageField(max_length=100, upload_to="image/%Y/%m", default="image/default.png")
    home = models.CharField(max_length=100, verbose_name="家地址", default="")
    company = models.CharField(max_length=100, verbose_name="公司地址", default="")
    department = models.CharField(max_length=100, verbose_name="部门", default="")
    credit_score = models.IntegerField(default=100, verbose_name="信用积分")
    money = models.CharField(max_length=100, verbose_name="余额", default="")
    
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.username


# 首页广告轮播
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(max_length=200, verbose_name="轮播图")
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
