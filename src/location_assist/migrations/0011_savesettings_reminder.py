# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-16 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_assist', '0010_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='savesettings',
            name='reminder',
            field=models.TextField(null=True),
        ),
    ]
