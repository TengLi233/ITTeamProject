# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotPotWebsite', '0002_auto_20180315_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menucategory',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='menucategory',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
