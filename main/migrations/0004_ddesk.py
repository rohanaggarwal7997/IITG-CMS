# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-01 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='ddesk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('link', models.URLField()),
            ],
        ),
    ]