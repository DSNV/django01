# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-23 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20190822_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companies',
            options={'verbose_name_plural': '[3]公司列表'},
        ),
        migrations.AlterModelOptions(
            name='founders',
            options={'verbose_name_plural': '[5]创始人'},
        ),
        migrations.AlterModelOptions(
            name='informations',
            options={'verbose_name_plural': '[2]招聘信息'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '[4]公司产品'},
        ),
        migrations.AlterModelOptions(
            name='resumeonline',
            options={'verbose_name_plural': '[]在线简历'},
        ),
        migrations.AlterModelOptions(
            name='resumes',
            options={'verbose_name_plural': '[]简历文件'},
        ),
        migrations.AlterField(
            model_name='positions',
            name='count',
            field=models.IntegerField(default=0, verbose_name='访问次数'),
        ),
        migrations.AlterField(
            model_name='positionstwo',
            name='shang',
            field=models.IntegerField(default=1, verbose_name='上级标签'),
        ),
        migrations.AlterField(
            model_name='positionstwo',
            name='xia',
            field=models.IntegerField(default=1, verbose_name='下级领域'),
        ),
        migrations.AlterField(
            model_name='postionsone',
            name='shang',
            field=models.IntegerField(default=0, verbose_name='上级领域'),
        ),
        migrations.AlterField(
            model_name='postionsone',
            name='xia',
            field=models.IntegerField(default=1, verbose_name='下级领域'),
        ),
        migrations.AlterField(
            model_name='resumes',
            name='resume',
            field=models.FileField(null=True, upload_to='', verbose_name='简历文件'),
        ),
    ]
