from datetime import datetime

from django.db import models


# 司机信息
class DriverProfile(models.Model):
    nick_name = models.CharField(max_length=30, verbose_name="昵称", default="老司机")
    birday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=((0, "男"), (1, "女")), default="男", help_text="性别 0/1 - 男/女")
    address = models.CharField(max_length=100, default="固戍A口", verbose_name="家地址", blank=True)
    mobile = models.CharField(max_length=11, null=True, default="1316xxxx2644", blank=True)
    image = models.ImageField(max_length=100, upload_to="examine/image/%Y%m%d", blank=True,
                              default="examine/images/default.png")
    credit_score = models.IntegerField(default=100, verbose_name="信用积分")
    status = models.CharField(max_length=11, null=True, choices=((0, "待审核"), (2, "吊销"), (1, "正常")), default="待审核",
                              verbose_name="司机状态")
    company = models.CharField(max_length=100, verbose_name="公司名称", default="", blank=True)
    company_address = models.CharField(max_length=100, verbose_name="公司地址", default="", blank=True)
    department = models.CharField(max_length=100, verbose_name="部门", default="", blank=True)
    money = models.CharField(max_length=100, verbose_name="余额", default=0)
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
