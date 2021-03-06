# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-01-16 12:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20200116_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='m_order',
            field=models.ForeignKey(help_text='主订单 id', null=True, on_delete=django.db.models.deletion.CASCADE, to='order.DriverOrder', verbose_name='主订单 id'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='r_status',
            field=models.CharField(choices=[('n', '待预定'), ('y', '已预订')], default='n', help_text='订单状态 y/n - 已预订/待预订', max_length=30, verbose_name='订单状态'),
        ),
    ]
