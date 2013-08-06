"""Tests that verify the functionality of the program from the end user's perspective."""
__author__ = 'ADillon'

from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title
