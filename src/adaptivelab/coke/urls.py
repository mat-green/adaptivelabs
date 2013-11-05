#  -*- coding: utf-8 -*-
'''
Created on Nov 5, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''

from django.conf.urls import patterns, url

from coke import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)