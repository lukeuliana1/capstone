# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-26 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20160422_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='trello',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]