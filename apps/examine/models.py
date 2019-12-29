from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# 司机信息
class DriverProfile(models.Model):
    user_id = models.ForeignKey(User, verbose_name="用户", null=True)
    driver_score = models.IntegerField(default=100, verbose_name="信用积分")
    driver_status = models.CharField(max_length=11, null=True, choices=((0, "待审核"), (2, "吊销"), (1, "正常")),
                                     default="待审核", verbose_name="司机状态")
    driver_money = models.CharField(max_length=100, verbose_name="余额", default=0)
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "司机信息"
        verbose_name_plural = verbose_name


# 审核记录
class ExamineLog(models.Model):
    applicant = models.ForeignKey(DriverProfile, verbose_name="司机 id", help_text="司机 id")
    license = models.ImageField(verbose_name="驾照", default="", blank=True)
    f_id_card = models.ImageField(verbose_name="身份证正面照", default="", blank=True)
    b_id_card = models.ImageField(verbose_name="身份证背面照", default="", blank=True)
    f_car = models.ImageField(verbose_name="车正面照", default="", blank=True)
    l_car = models.ImageField(verbose_name="车左侧照", default="", blank=True)
    r_car = models.ImageField(verbose_name="车右侧照", default="", blank=True)
    status = models.CharField(max_length=30, null=True, choices=((0, "待审核"), (2, "未通过"), (1, "通过")), default=0,
                              verbose_name="审核状态 0/1/2 - 待审核/通过/未通过")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "审核记录"
        verbose_name_plural = verbose_name


# 司机违规条目
class FoulRule(models.Model):
    s_name = models.CharField(max_length=6, verbose_name="简称")
    msg = models.CharField(max_length=6, verbose_name="条目注释", default="", blank=True)
    deduction = models.IntegerField(default=0, verbose_name="扣分值")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "司机违规条目"
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
