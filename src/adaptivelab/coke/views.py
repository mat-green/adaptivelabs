#  -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from coke.controllers import Fetcher
from coke.models import Tweet

class MessagesView(TemplateView):
    '''
    API provider view that generates the tweets if they are successfully retrieved.
    '''
    
    template_name = 'messages.json'
    
    def get_context_data(self, **kwargs):
        context = super(MessagesView, self).get_context_data(**kwargs)
        ctrl = Fetcher()
        if(ctrl.execute()):
            data = Tweet.objects.all().order_by('-sentiment')
            context.update({
                'tweets': data
            })
        return context
