# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime

from portfolio.models import Project


def index(request):
    print(request.META['REMOTE_ADDR'])
    portfolio_time = datetime.now()
    list_of_projects = Project.objects.order_by('pub_date')
    return render(request, 'portfolio/index.html', {'portfolio_time': portfolio_time, 'list_of_projects': list_of_projects})
