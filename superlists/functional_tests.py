"""Tests that verify the functionality of the program from the end user's perspective."""
__author__ = 'ADillon'

from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. She goes to check out its homepage
browser.get("http://localhost:8000")

# She notices the title and header mention to-do lists
assert "To-Do" in browser.title

# She is invited to enter a to-do item straight away

# She types "Buy milk" into a text box

# When she hits 'Enter', the page updates, and now the page lists "1: Buy milk"

# There is still a text box inviting her to add another item.

# She enters "Buy eggs" and presses 'Enter' to see "2: Buy eggs" added to her list

# Edith sees that the site has generated a URL for her to revisit her to-do list in the future

# There is some explanatory text regarding the URL

# She visits the URL to see that her to-do list is still there

# Satisfied, Edith goes back to sleep

browser.quit()
