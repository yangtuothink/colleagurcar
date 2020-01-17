# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2020-01-16 10:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriverMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, default='', help_text='信息内容', max_length=500, verbose_name='信息内容')),
                ('has_read', models.CharField(blank=True, choices=[('y', '已读'), ('n', '未读')], default='y', help_text='是否已读 n/y - 未/已', max_length=30, verbose_name='是否已读')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '系统信息推送司机',
                'verbose_name_plural': '系统信息推送司机',
            },
        ),
        migrations.CreateModel(
            name='DriverProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_score', models.IntegerField(default=100, verbose_name='信用积分')),
                ('driver_status', models.CharField(choices=[('g', '待审核'), ('b', '吊销'), ('n', '正常')], default='g', max_length=11, null=True, verbose_name='司机状态')),
                ('driver_money', models.CharField(default=0, max_length=100, verbose_name='余额')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '司机信息',
                'verbose_name_plural': '司机信息',
            },
        ),
        migrations.CreateModel(
            name='ExamineLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.ImageField(blank=True, default='', help_text='驾照', upload_to='examine/images/%Y%m%d', verbose_name='驾照')),
                ('f_id_card', models.ImageField(blank=True, default='', help_text='身份证正面照', upload_to='examine/images/%Y%m%d', verbose_name='身份证正面照')),
                ('b_id_card', models.ImageField(blank=True, default='', help_text='身份证背面照', upload_to='examine/images/%Y%m%d', verbose_name='身份证背面照')),
                ('f_car', models.ImageField(blank=True, default='', help_text='车正面照', upload_to='examine/images/%Y%m%d', verbose_name='车正面照')),
                ('l_car', models.ImageField(blank=True, default='', help_text='车左侧照', upload_to='examine/images/%Y%m%d', verbose_name='车左侧照')),
                ('r_car', models.ImageField(blank=True, default='', help_text='车后侧照', upload_to='examine/images/%Y%m%d', verbose_name='车后侧照')),
                ('status', models.CharField(choices=[('n', '待审核'), ('b', '未通过'), ('g', '通过')], default='n', max_length=30, null=True, verbose_name='审核状态 n/g/b - 待审核/通过/未通过')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('applicant', models.ForeignKey(help_text='司机 id', on_delete=django.db.models.deletion.CASCADE, to='examine.DriverProfile', verbose_name='司机 id')),
            ],
            options={
                'verbose_name': '审核记录',
                'verbose_name_plural': '审核记录',
            },
        ),
        migrations.CreateModel(
            name='FoulLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('applicant', models.ForeignKey(help_text='违规人 -  司机 id', on_delete=django.db.models.deletion.CASCADE, to='examine.DriverProfile', verbose_name='违规人 - 司机 id')),
            ],
            options={
                'verbose_name': '违规记录',
                'verbose_name_plural': '违规记录',
            },
        ),
        migrations.CreateModel(
            name='FoulRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=6, verbose_name='简称')),
                ('msg', models.CharField(blank=True, default='', max_length=6, verbose_name='条目注释')),
                ('deduction', models.IntegerField(default=0, verbose_name='扣分值')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '司机违规条目',
                'verbose_name_plural': '司机违规条目',
            },
        ),
        migrations.AddField(
            model_name='foullog',
            name='foul_rule',
            field=models.ForeignKey(help_text='违规条目 id', on_delete=django.db.models.deletion.CASCADE, to='examine.FoulRule', verbose_name='违规条目 id'),
        ),
    ]
