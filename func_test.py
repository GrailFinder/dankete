#!/usr/bin/env python
from selenium import webdriver
import unittest, os


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        print(os.getcwd())
        chromedriver_path = os.path.join(os.getcwd(), "closet/geckodriver")
        print(chromedriver_path)
        self.browser = webdriver.Firefox(executable_path="closet/geckodriver")

    def tearDown(self):
        self.browser.quit()

    def test_edith_tries_the_site(self):
        # Edith heards about online questionaire so she visits home page
        self.browser.get("http://localhost:8000")

        # sees Django it title (what a odd thing to see)
        assert "Django" in self.browser.title

        # she follows to inquires page
        self.browser.find_element_by_xpath("//a[contains(@href, 'inqs')]").click()
        assert "Inquiry List" in self.browser.page_source

        # picks: WHo are you from the Star Wars? query
        assert "Who are you from the Star Wars?" in self.browser.page_source

        # checks some checkboxes/radio buttons and clicks submit button

        # page returns answer: You're Bobba Fett


if __name__ == "__main__":
    unittest.main(warnings="ignore")