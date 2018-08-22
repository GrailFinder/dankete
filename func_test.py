from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_edith_tries_the_site(self):
        # Edith heards about online questionaire so she visits home page
        self.browser.get("http://localhost:8000")

        # sees Django it title (what a odd thing to see)
        assert "Django" in self.browser.title

        # she follows to inquires page

        # picks: WHo are you from the Star Wars? query

        # checks some checkboxes/radio buttons and clicks submit button

        # page returns answer: You're Bobba Fett


if __name__ == "__main__":
    unittest.main(warnings="ignore")