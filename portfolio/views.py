# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from datetime import datetime
from .models import Project


class IndexView(ListView):

    template_name = 'portfolio/index.html'
    model = Project
    queryset = Project.objects.order_by('pub_date')
    context_object_name = 'list_of_projects'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['portfolio_time'] = datetime.now()
        return context


class DetailView(DetailView):

    template_name = 'portfolio/detail.html'
    model = Project
