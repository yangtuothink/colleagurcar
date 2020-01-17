# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-01-17 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_coursecomments_m_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancellog',
            name='m_order',
            field=models.ForeignKey(help_text='订单 id', null=True, on_delete=django.db.models.deletion.CASCADE, to='order.DriverOrder', verbose_name='订单'),
        ),
    ]
