#  -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from coke.testpages import IndexPage


class IndexPageTest(LiveServerTestCase):
    """Execution via: python manage.py test coke.IndexPageTest"""
    
    @classmethod
    def setUpClass(cls):
        super(IndexPageTest, cls).setUpClass()
        cls.selenium = WebDriver()
        
        
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()    
        super(IndexPageTest, cls).tearDownClass()
        
    
    def test_index_page_access(self):
        """
        Tests the index page can be accessed.
        """
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        page = IndexPage(self.selenium)
