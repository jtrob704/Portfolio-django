# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20171229_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='year',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_year',
            field=models.IntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_year',
            field=models.IntegerField(default=2000),
        ),
    ]