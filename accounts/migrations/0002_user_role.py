# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-29 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.BooleanField(default=True, verbose_name='Role'),
        ),
    ]
