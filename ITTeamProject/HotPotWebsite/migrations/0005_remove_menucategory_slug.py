# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotPotWebsite', '0004_auto_20180315_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menucategory',
            name='slug',
        ),
    ]
