# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20171229_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='year',
            field=models.IntegerField(default=2017),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_year',
            field=models.IntegerField(default=2017),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_year',
            field=models.IntegerField(default=2000),
        ),
    ]