# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from taggit.models import Tag
from .models import Project, Screenshot


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['portfolio_time'] = timezone.now()
        return context


class IndexView(TagMixin, ListView):

    template_name = 'portfolio/index.html'
    model = Project
    paginate_by = '3'
    queryset = Project.objects.order_by('pub_date').prefetch_related('tags')
    context_object_name = 'list_of_projects'


class DetailView(DetailView):
    
    template_name = 'portfolio/detail.html'
    model = Project


class TagView(TagMixin, ListView):

    template_name = 'portfolio/index.html'
    model = Project
    paginate_by = '3'
    context_object_name = 'list_of_projects'     

    def get_queryset(self):
        return Project.objects.filter(tags__slug=self.kwargs.get('slug')).order_by('pub_date').prefetch_related('tags')