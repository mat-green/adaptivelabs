#  -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request, { })
    return HttpResponse(template.render(context))
