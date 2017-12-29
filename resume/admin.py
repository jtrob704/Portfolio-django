# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Resume, Skills, Experience, Education

class SkillsInline(admin.StackedInline):
    model = Skills


class ExperienceInline(admin.StackedInline):
    model = Experience


class EducationInline(admin.StackedInline):
    model = Education

class ResumeAdmin(admin.ModelAdmin):
    inlines = [SkillsInline, ExperienceInline, EducationInline]

# Register your models here.
admin.site.register(Resume, ResumeAdmin)