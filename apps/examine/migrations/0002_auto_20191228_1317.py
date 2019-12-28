# Generated by Django 3.0.1 on 2019-12-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinelog',
            name='b_id_card',
            field=models.ImageField(default='', upload_to='', verbose_name='身份证背面照'),
        ),
        migrations.AddField(
            model_name='examinelog',
            name='f_car',
            field=models.ImageField(default='', upload_to='', verbose_name='车正面照'),
        ),
        migrations.AddField(
            model_name='examinelog',
            name='f_id_card',
            field=models.ImageField(default='', upload_to='', verbose_name='身份证正面照'),
        ),
        migrations.AddField(
            model_name='examinelog',
            name='l_car',
            field=models.ImageField(default='', upload_to='', verbose_name='车左侧照'),
        ),
        migrations.AddField(
            model_name='examinelog',
            name='r_car',
            field=models.ImageField(default='', upload_to='', verbose_name='车右侧照'),
        ),
    ]
