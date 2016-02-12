# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import project.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('description', models.TextField()),
                ('github', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to=project.models.image_upload_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('employees', models.ForeignKey(to='account.Employee')),
                ('students', models.ForeignKey(to='account.Student')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-created'],
            },
        ),
    ]
