# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20171229_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='year',
            field=models.IntegerField(default=2017, max_length=4),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_year',
            field=models.IntegerField(default=2017, max_length=4),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_year',
            field=models.IntegerField(default=2000, max_length=4),
        ),
    ]