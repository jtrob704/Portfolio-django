# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 19:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_technology'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'technologies'},
        ),
    ]