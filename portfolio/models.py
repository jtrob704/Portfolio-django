# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    URL = models.URLField(max_length=200)
    screenshot = models.ImageField(upload_to='screenshots')
    screenshot_thumbnail = ImageSpecField(source='screenshot',
                                          processors=[ResizeToFill(300, 200)],
                                          format='PNG',
                                          options={'quality': 60})
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name
