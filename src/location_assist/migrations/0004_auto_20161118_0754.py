# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-18 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_assist', '0003_auto_20161118_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendlist',
            name='friendList',
            field=models.TextField(),
        ),
    ]