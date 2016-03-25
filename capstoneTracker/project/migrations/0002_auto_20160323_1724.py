# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employees',
        ),
        migrations.RemoveField(
            model_name='project',
            name='students',
        ),
        migrations.AddField(
            model_name='project',
            name='brief_description',
            field=models.CharField(max_length=300, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
