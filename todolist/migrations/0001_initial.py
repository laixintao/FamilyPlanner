# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-29 14:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_user_role'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=300, verbose_name='Task')),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_todo', to='accounts.Family')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_todo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
