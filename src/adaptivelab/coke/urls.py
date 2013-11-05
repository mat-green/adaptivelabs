#  -*- coding: utf-8 -*-
'''
Created on Nov 5, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''

from django.conf.urls import patterns, url

from coke.views import MessagesView
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^api/messages/$', MessagesView.as_view(), name='messages'),
)