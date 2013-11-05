#  -*- coding: utf-8 -*-
'''
Created on Nov 5, 2013

@author: "Matthew Green<matthew@newedgeengineering.com>"
'''

import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,\
    WebDriverException

class IndexPage(unittest.TestCase):
    
    def __init__(self, driver, wait=10000):
        self.driver = driver
        self.wait = wait
        self.assertEquals(u'Adaptive Lab\'s Technical Test', driver.title)
        
        
    def ajax_complete(self, driver):
        try:
            return 0 == driver.execute_script("return jQuery.active")
        except WebDriverException:
            pass
        
        
    def clickFetch(self):
        self.driver.find_element_by_xpath('//button[text()="Fetch Messages"]').click()
        #wait for ajax items to load
        WebDriverWait(self.driver, 10).until(
             self.ajax_complete,  "Timeout waiting for page to load")
        return IndexPage(self.driver, self.wait)
    
    
    def checkForError(self):
        try:
            self.driver.find_element_by_xpath('//p[contains(text(), "OOPS!")]')
            return True
        except NoSuchElementException:
            return False
    
    
    def checkForMessages(self):
        try:
            self.driver.find_element_by_xpath('//dl')
            return True
        except NoSuchElementException:
            return False
        