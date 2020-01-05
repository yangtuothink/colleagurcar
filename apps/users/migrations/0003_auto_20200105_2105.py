# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-01-05 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_is_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[(0, '男'), (1, '女')], default=0, help_text='性别  0/1 - 男/女', max_length=6, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_driver',
            field=models.CharField(choices=[(0, '否'), (1, '是')], default=0, help_text='是否司机', max_length=100, verbose_name='是否司机'),
        ),
    ]
