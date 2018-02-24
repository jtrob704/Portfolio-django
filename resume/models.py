# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.

YEAR_CHOICES = []
for r in range(1990, (datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

def current_year():
    return datetime.now().year


class Resume(models.Model):
    title = models.CharField(max_length = 30)    
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
    job_description = models.TextField()
    year = models.IntegerField(choices=YEAR_CHOICES, default=current_year())

class Education(models.Model):
    class Meta:
        verbose_name_plural = "education"
    
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school_name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 2)    
    year = models.IntegerField(choices=YEAR_CHOICES, default=current_year())