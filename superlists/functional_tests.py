"""Tests that verify the functionality of the program from the end user's perspective."""
__author__ = 'ADillon'

import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # She is invited to enter a to-do item straight away

        # She types "Buy milk" into a text box

        # When she hits 'Enter', the page updates, and now the page lists "1: Buy milk"

        # There is still a text box inviting her to add another item.

        # She enters "Buy eggs" and presses 'Enter' to see "2: Buy eggs" added to her list

        # Edith sees that the site has generated a URL for her to revisit her to-do list in the future

        # There is some explanatory text regarding the URL

        # She visits the URL to see that her to-do list is still there

        # Satisfied, Edith goes back to sleep


if __name__ == "__main__":
    unittest.main()