# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-21 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'education',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=30)),
                ('job_description', models.TextField()),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'experience',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=30)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Resume')),
            ],
            options={
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
        migrations.AddField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Resume'),
        ),
    ]
