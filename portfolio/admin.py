# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Project, Screenshot

class ScreenshotInline(admin.StackedInline):
    model = Screenshot
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [ScreenshotInline]

# Register your models here.
admin.site.register(Project, PortfolioAdmin)