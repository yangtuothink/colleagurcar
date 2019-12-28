from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户表 - 继承
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="阿一", help_text="昵称")
    birday = models.DateField(verbose_name="生日", null=True, help_text="生日")
    gender = models.CharField(max_length=6, verbose_name="性别", choices=((0, "男"), (1, "女")), default="男",
                              help_text="性别  0/1 - 男/女")
    address = models.CharField(max_length=100, default="", blank=True, help_text="地址")
    mobile = models.CharField(max_length=11, default="1316XXXX1236", help_text="电话")
    image = models.ImageField(max_length=100, verbose_name="头像", upload_to="users/images/%Y%m%d",
                              default="users/images/default.png", help_text="头像")
    home = models.CharField(max_length=100,verbose_name="家地址", default="", blank=True, help_text="家地址")
    company_address = models.CharField(max_length=100, verbose_name="公司地址", default="", blank=True, help_text="公司地址")
    company = models.CharField(max_length=100, verbose_name="公司名称", default="", blank=True, help_text="公司名称")
    department = models.CharField(max_length=100, verbose_name="部门", default="", blank=True, help_text="部门")
    credit_score = models.IntegerField(default=100, verbose_name="信用积分", help_text="信用积分")
    money = models.CharField(max_length=100, verbose_name="余额", default=0, help_text="余额")
    
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.username


# 首页广告轮播
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题", null=True, help_text="标题")
    image = models.ImageField(max_length=200, verbose_name="轮播图", help_text="轮播图")
    url = models.URLField(max_length=200, verbose_name="访问地址", blank=True, null=True, help_text="访问地址")
    index = models.IntegerField(default=1, verbose_name="顺序", help_text="顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
