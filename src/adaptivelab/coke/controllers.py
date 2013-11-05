#  -*- coding: utf-8 -*-
'''
Created on Nov 5, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''
import requests

class Fetcher(object):
    '''
    Command controller to fetch messages
    '''
    
    
    __HEAD_URL__ = "http://adaptive-test-api.herokuapp.com/"
    __DATA_URL__ = "http://adaptive-test-api.herokuapp.com/tweets.json"
    
    def __init__(self):
        self.model = []
    
    def execute(self):
        check = requests.head(self.__HEAD_URL__)
        if(check.status_code == 200):
            result = requests.get(self.__DATA_URL__)
            if(result.status_code == 200):
                self.model = result.json()
                return True
            else:
                return False
        else:
            return False