# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-01-29 16:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200129_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 29, 16, 58, 50, 152710), verbose_name='添加时间'),
        ),
    ]
