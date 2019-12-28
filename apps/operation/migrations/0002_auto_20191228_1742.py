# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-12-28 17:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('examine', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermessage',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='接收人'),
        ),
        migrations.AddField(
            model_name='coursecomments',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='顾客'),
        ),
        migrations.AddField(
            model_name='coursecomments',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examine.DriverProfile', verbose_name='司机'),
        ),
        migrations.AddField(
            model_name='coursecomments',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='订单'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='订单'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发送人'),
        ),
        migrations.AddField(
            model_name='cancellog',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='顾客'),
        ),
        migrations.AddField(
            model_name='cancellog',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examine.DriverProfile', verbose_name='司机'),
        ),
        migrations.AddField(
            model_name='cancellog',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='订单'),
        ),
    ]
