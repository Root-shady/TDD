from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page


# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page) # finda  function call home_page

    def test_home_page_returns_correct_html(self):
        request= HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        # Use decode to convert the repsonse.content bytes into a Python unicode string
        self.assertEqual(response.content.decode(), expected_html)






