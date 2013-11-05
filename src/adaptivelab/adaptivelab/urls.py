#  -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('coke.urls')),
    # Examples:
    # url(r'^$', 'adaptivelab.views.home', name='home'),
    # url(r'^adaptivelab/', include('adaptivelab.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
