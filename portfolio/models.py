# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager
from autoslug import AutoSlugField


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',null=True)
    description = models.TextField()
    URL = models.URLField(max_length=200)    
    main_index_thumbnail = ProcessedImageField(upload_to='screenshots',
                                               processors=[ResizeToFill(300, 200)],
                                               format='PNG',
                                               options={'quality': 60},
                                               null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        from portfolio.urls import urlpatterns
        return reverse('detail', args=[str(self.slug)])


class Screenshot(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots')
    screenshot_thumbnail = ImageSpecField(source='screenshot',
                                          processors=[ResizeToFill(300, 200)],
                                          format='PNG',
                                          options={'quality': 60})
