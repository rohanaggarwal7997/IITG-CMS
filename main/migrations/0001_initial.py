# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('image_url', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('link', models.URLField()),
            ],
        ),
    ]
