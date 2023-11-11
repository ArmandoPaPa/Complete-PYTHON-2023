from locators.quote_locators import QuoteLocators
from selenium.webdriver.common.by import By


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"<Quote {self.content}, by {self.author}>"

    @property
    def content(self):
        locator = QuoteLocators.CONTENT_LOCATOR
        # return self.parent.find_element_by_css_selector(locator).text
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR_LOCATOR
        # return self.parent.find_element_by_css_selector(locator).text
        return self.parent.find_element(By.CSS_SELECTOR, locator).text

    @property
    def tag(self):
        locator = QuoteLocators.TAGS_LOCATOR
        # return self.parent.find_elements_by_css_selector(locator)
        return self.parent.find_elements(By.CSS_SELECTOR, locator)