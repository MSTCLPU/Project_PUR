# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 13:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20170817_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operations',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 8, 17, 13, 18, 29, 943752, tzinfo=utc)),
        ),
    ]
