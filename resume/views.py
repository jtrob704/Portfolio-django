# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from .models import Resume, Skills, Experience, Education

# Create your views here.
class ResumeView(ListView):

    template_name = 'resume/index.html'
    model = Resume
    queryset = Resume.objects.all()
    context_object_name = 'list_of_resumes'

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['active_page'] = "resume"
        context['list_of_skills'] = Skills.objects.all()
        context['list_of_experience'] = Experience.objects.all()
        context['list_of_education'] = Education.objects.all()
        return context