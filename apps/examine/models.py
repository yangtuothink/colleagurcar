from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# 司机信息
class DriverProfile(models.Model):
    driver_name = models.CharField(max_length=50, verbose_name="司机名", default="帅司机")
    user_id = models.ForeignKey(User, verbose_name="用户", null=True)
    driver_score = models.IntegerField(default=100, verbose_name="信用积分")
    driver_status = models.CharField(max_length=11, null=True, choices=(("g", "待审核"), ("b", "吊销"), ("n", "正常")),
                                     default="g", verbose_name="司机状态")
    driver_money = models.CharField(max_length=100, verbose_name="余额", default=0)
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "司机信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.driver_name


# 审核记录
class ExamineLog(models.Model):
    applicant = models.ForeignKey(DriverProfile, verbose_name="司机 id", help_text="司机 id")
    license = models.ImageField(verbose_name="驾照", upload_to="examine/images/%Y%m%d", default="", blank=True,
                                help_text="驾照")
    f_id_card = models.ImageField(verbose_name="身份证正面照", upload_to="examine/images/%Y%m%d", default="", blank=True,
                                  help_text="身份证正面照")
    b_id_card = models.ImageField(verbose_name="身份证背面照", upload_to="examine/images/%Y%m%d", default="", blank=True,
                                  help_text="身份证背面照")
    f_car = models.ImageField(verbose_name="车正面照", upload_to="examine/images/%Y%m%d", default="", blank=True,
                              help_text="车正面照")
    l_car = models.ImageField(verbose_name="车左侧照", upload_to="examine/images/%Y%m%d", default="", blank=True,
                              help_text="车左侧照")
    r_car = models.ImageField(verbose_name="车后侧照", upload_to="examine/images/%Y%m%d", default="", blank=True,
                              help_text="车后侧照")
    status = models.CharField(max_length=30, null=True, choices=(("n", "待审核"), ("b", "未通过"), ("g", "通过")), default="n",
                              verbose_name="审核状态 n/g/b - 待审核/通过/未通过")
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
    has_read = models.CharField(max_length=30, default="y", choices=(("y", "已读"), ("n", "未读")), verbose_name="是否已读",
                                blank=True, help_text="是否已读 n/y - 未/已")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "系统信息推送司机"
        verbose_name_plural = verbose_name
