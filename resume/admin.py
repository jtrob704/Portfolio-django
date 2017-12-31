# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Resume, Skills, Experience, Education

class SkillsInline(admin.StackedInline):
    model = Skills
    extra = 1


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ResumeAdmin(admin.ModelAdmin):
    inlines = [SkillsInline, ExperienceInline, EducationInline]

# Register your models here.
admin.site.register(Resume, ResumeAdmin)