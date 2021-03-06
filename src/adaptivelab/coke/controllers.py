#  -*- coding: utf-8 -*-
'''
Created on Nov 5, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''
import requests
from coke.models import Tweet
import re

class Fetcher(object):
    '''
    Command controller to fetch messages
    '''
    
    
    __HEAD_URL__ = "http://adaptive-test-api.herokuapp.com/"
    __DATA_URL__ = "http://adaptive-test-api.herokuapp.com/tweets.json"
    
    
    def execute(self):
        '''
        process execution that does the following:
        * retrieves tweets
        * marks up coke, coco-cola and diet cola as red
        * persists the data within the Tweet model
        * increments the occurance if tweet has already been seen.
        '''
        check = requests.head(self.__HEAD_URL__)
        if(check.status_code == 200):
            result = requests.get(self.__DATA_URL__)
            if(result.status_code == 200):
                for data in result.json():
                    message = data["message"]
                    m = re.search("(coke)|(Coke)|(coca-cola)|(diet cola)", message)
                    if m:
                        for text in m.groups():
                            if text:
                                message = message.replace(text, '<span class=\\"red\\">%s</span>' % text)
                    try:
                        existing = Tweet.objects.get(message=message, user_handle=data["user_handle"])
                        existing.occurances = existing.occurances+1
                        existing.save()
                    except Tweet.DoesNotExist:
                        model = Tweet(message=message,
                                      sentiment=data["sentiment"],
                                      user_handle=data["user_handle"])
                        model.save()
                return True
            else:
                return False
        else:
            return False
        