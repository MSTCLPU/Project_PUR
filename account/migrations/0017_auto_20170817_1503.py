# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 15:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20170817_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operations',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 8, 17, 15, 3, 40, 899603, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='operations',
            name='mobile',
            field=models.IntegerField(verbose_name=12),
        ),
    ]
