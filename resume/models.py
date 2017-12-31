# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Skills(models.Model):
    class Meta:
        verbose_name_plural = "skills"
    
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length = 30)

class Experience(models.Model):
    class Meta:
        verbose_name_plural = "experience"

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_title = models.CharField(max_length = 30)
    start_year = models.IntegerField(default = 2000)
    end_year = models.IntegerField(default = datetime.now().year)

class Education(models.Model):
    class Meta:
        verbose_name_plural = "education"
    
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school_name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 2)
    year = models.IntegerField(default = datetime.now().year)