# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
