# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotPotWebsite', '0005_remove_menucategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='menucategory',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
