# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-01-13 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examine', '0003_auto_20200105_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examinelog',
            name='b_id_card',
            field=models.ImageField(blank=True, default='', help_text='身份证背面照', upload_to='examine/images/%Y%m%d', verbose_name='身份证背面照'),
        ),
        migrations.AlterField(
            model_name='examinelog',
            name='f_car',
            field=models.ImageField(blank=True, default='', help_text='车正面照', upload_to='examine/images/%Y%m%d', verbose_name='车正面照'),
        ),
        migrations.AlterField(
            model_name='examinelog',
            name='f_id_card',
            field=models.ImageField(blank=True, default='', help_text='身份证正面照', upload_to='examine/images/%Y%m%d', verbose_name='身份证正面照'),
        ),
        migrations.AlterField(
            model_name='examinelog',
            name='l_car',
            field=models.ImageField(blank=True, default='', help_text='车左侧照', upload_to='examine/images/%Y%m%d', verbose_name='车左侧照'),
        ),
        migrations.AlterField(
            model_name='examinelog',
            name='license',
            field=models.ImageField(blank=True, default='', help_text='驾照', upload_to='examine/images/%Y%m%d', verbose_name='驾照'),
        ),
        migrations.AlterField(
            model_name='examinelog',
            name='r_car',
            field=models.ImageField(blank=True, default='', help_text='车后侧照', upload_to='examine/images/%Y%m%d', verbose_name='车后侧照'),
        ),
    ]