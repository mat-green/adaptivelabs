#  -*- coding: utf-8 -*-
'''
Created on Nov 5, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''

import unittest

class IndexPage(unittest.TestCase):
    
    def __init__(self, driver, wait=10000):
        self.driver = driver
        self.wait = wait
        self.assertEquals(u'', driver.title)