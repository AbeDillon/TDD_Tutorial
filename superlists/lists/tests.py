"""
Unit tests for the basic list app
"""

from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page


class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		"""
		Tests that the root URL resolves to this app's homepage
		"""
		found = resolve("/")
		self.assertEqual(found.func, home_page)
