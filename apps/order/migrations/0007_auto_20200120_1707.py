# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-01-20 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0006_cancellog_m_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='m_order',
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='sender',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='initiator',
            field=models.ForeignKey(default='', help_text='发送人 id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发送人 id'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='is_driver',
            field=models.CharField(choices=[('n', '否'), ('y', '是')], default='n', help_text='是否司机', max_length=100, verbose_name='是否司机'),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='has_read',
            field=models.CharField(choices=[('n', '未读'), ('y', '已读')], default='n', help_text='是否已读 n/y - 未读/已读', max_length=30, verbose_name='是否已读'),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='pay_status',
            field=models.CharField(choices=[('0', '已发布待接单'), ('1', '行程待开始'), ('2', '行程中'), ('3', '待支付'), ('4', '已关闭'), ('5', '已完成'), ('6', '已取消')], default=0, help_text='订单状态 0/1/2/3/4/5 - 已发布待预约/行程待开始/行程中/待支付/已关闭/已完成', max_length=30, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='driverorder',
            name='pay_status',
            field=models.CharField(choices=[('0', '已发布待预约'), ('1', '已预约待出发'), ('2', '行程中'), ('3', '待支付'), ('4', '已关闭'), ('5', '已完成'), ('6', '已取消')], default=0, help_text='订单状态 0/1/2/3/4/5/6 - 已发布待预约/已预约待出发/行程中/待支付/已关闭/已完成/已取消', max_length=30, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='driverorder',
            name='r_status',
            field=models.CharField(choices=[('n', '待预定'), ('y', '已预订')], default='n', help_text='订单状态 y/n - 已预订/待预定', max_length=30, verbose_name='订单状态'),
        ),
    ]
