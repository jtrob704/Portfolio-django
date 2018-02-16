# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import  TemplateView

# Create your views here.
class HomepageView(TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):    
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['active_page'] = "home"
        return context