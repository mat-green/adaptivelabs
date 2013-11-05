#  -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from coke.controllers import Fetcher

class MessagesView(TemplateView):
    
    template_name = 'messages.json'
    
    def get_context_data(self, **kwargs):
        context = super(MessagesView, self).get_context_data(**kwargs)
        ctrl = Fetcher()
        if(ctrl.execute()):
            context.update({
                'tweets': ctrl.model
            })
        return context
