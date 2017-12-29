# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Skills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length = 30)

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_title = models.CharField(max_length = 30)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school_name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 2)
    year = models.IntegerField()