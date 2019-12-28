from datetime import datetime

from django.db import models


# 司机信息
class DriverProfile(models.Model):
    nick_name = models.CharField(max_length=30, verbose_name="昵称")
    birday = models.DateField(verbose_name="生日", null=True)
    gender = models.CharField(max_length=6, choices=(("", "男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default="", verbose_name="家地址")
    mobile = models.CharField(max_length=11, null=True, default="")
    image = models.ImageField(max_length=100)
    credit_score = models.IntegerField(default=100, verbose_name="信用积分")
    status = models.CharField(max_length=11, null=True, choices=((0, "待审核"), (2, "吊销"), (1, "正常")), default=0,
                              verbose_name="司机状态")
    company = models.CharField(max_length=100, verbose_name="公司地址", default="")
    department = models.CharField(max_length=100, verbose_name="部门", default="")
    money = models.CharField(max_length=100, verbose_name="余额", default="")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "司机信息"
        verbose_name_plural = verbose_name


# 审核记录
class ExamineLog(models.Model):
    applicant = models.CharField(max_length=30, verbose_name="申请人")
    gender = models.CharField(max_length=6, choices=(("", "男"), ("female", "女")), default="female")
    age = models.CharField(max_length=6)
    address = models.CharField(max_length=100, default="", verbose_name="住址")
    mobile = models.CharField(max_length=11, null=True, default="")
    license = models.ImageField(verbose_name="驾照")
    f_id_card = models.ImageField(verbose_name="身份证正面照", default="")
    b_id_card = models.ImageField(verbose_name="身份证背面照", default="")
    f_car = models.ImageField(verbose_name="车正面照", default="")
    l_car = models.ImageField(verbose_name="车左侧照", default="")
    r_car = models.ImageField(verbose_name="车右侧照", default="")
    status = models.CharField(max_length=11, null=True, choices=((0, "待审核"), (2, "未通过"), (1, "通过")), default=0,
                              verbose_name="审核状态")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "审核记录"
        verbose_name_plural = verbose_name


# 司机违规条目
class FoulRule(models.Model):
    s_name = models.CharField(max_length=6, verbose_name="简称", default="")
    msg = models.CharField(max_length=6, verbose_name="条目注释", default="")
    deduction = models.IntegerField(default=0, verbose_name="扣分值")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "司机违规条目"
        verbose_name_plural = verbose_name
