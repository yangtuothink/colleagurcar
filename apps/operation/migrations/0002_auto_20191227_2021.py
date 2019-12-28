# Generated by Django 3.0.1 on 2019-12-27 20:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('examine', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500, verbose_name='信息内容')),
                ('has_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='订单')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发送人')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(default=0, verbose_name='星级')),
                ('comments', models.CharField(max_length=200, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='顾客')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examine.DriverProfile', verbose_name='司机')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='订单')),
            ],
            options={
                'verbose_name': '行程评价',
                'verbose_name_plural': '行程评价',
            },
        ),
        migrations.CreateModel(
            name='FoulLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examine.DriverProfile', verbose_name='违规人')),
                ('foul_rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examine.FoulRule', verbose_name='违规条目')),
            ],
            options={
                'verbose_name': '违规记录',
                'verbose_name_plural': '违规记录',
            },
        ),
        migrations.CreateModel(
            name='SystemMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500, verbose_name='信息内容')),
                ('has_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='接收人')),
            ],
            options={
                'verbose_name': '系统信息推送',
                'verbose_name_plural': '系统信息推送',
            },
        ),
        migrations.DeleteModel(
            name='UserMessage',
        ),
    ]
