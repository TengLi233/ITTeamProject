# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotPotWebsite', '0003_auto_20180315_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
