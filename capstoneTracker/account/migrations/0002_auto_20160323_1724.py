# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20160323_1724'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='project',
            field=models.ForeignKey(to='project.Project', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='project',
            field=models.ForeignKey(to='project.Project', default=''),
            preserve_default=False,
        ),
    ]
