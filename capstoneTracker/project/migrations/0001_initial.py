# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
import project.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('brief_description', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('github', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to=project.models.image_upload_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name_plural': 'Projects',
                'verbose_name': 'Project',
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
