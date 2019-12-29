# -*- coding:utf-8 -*-
from datetime import datetime

from django.db import models

from order.models import Order


# 后台暗账
class DrakBill(models.Model):
    trade_no = models.ForeignKey(Order, to_field="trade_no", verbose_name="交易号", on_delete=models.CASCADE,
                                 help_text="交易号")
    admin_money = models.IntegerField(default=0, verbose_name="公司总账", help_text="公司总账")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
