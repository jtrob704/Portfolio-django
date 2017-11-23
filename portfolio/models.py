# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    URL = models.URLField(max_length=200)
    screenshot = models.ImageField(upload_to='screenshots')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
