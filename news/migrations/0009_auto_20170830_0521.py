# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0008_auto_20170830_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
