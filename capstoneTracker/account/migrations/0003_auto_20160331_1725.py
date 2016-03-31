# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160323_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='project',
            field=models.ForeignKey(blank=True, null=True, to='project.Project'),
        ),
    ]
