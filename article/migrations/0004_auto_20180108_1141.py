# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-01-08 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20180104_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=30, verbose_name='\u6587\u7ae0\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=1, verbose_name='\u6d4f\u89c8\u91cf'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u7c7b\u522b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20, verbose_name='\u6807\u7b7e\u540d\u79f0'),
        ),
    ]
