#from selenium import webdriver
#
#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')
#
#assert 'To-Do' in browser.title
#browser.quit()

#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
import unittest
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
    # A smoke test[The configuration of static file]
    def test_layout_and_styling(self):
        # Edit goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notice that input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] /2,
                512,
                delta=5
            )

