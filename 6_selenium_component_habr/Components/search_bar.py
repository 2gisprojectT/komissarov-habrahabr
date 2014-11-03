from selenium.webdriver.common.keys import Keys
from base_component import BaseComponent

__author__ = 'jk'
# -*- coding: utf-8 -*-


class SearchBar(BaseComponent):
    selectors = {
        'self': '#inner_search_form > input[name=\"q\"]',
        'sort_relevation': '.sort_menu > li:nth-child(2) > a:nth-child(1)',
        'sort_time': '.sort_menu > li:nth-child(3) > a:nth-child(1)',
        'sort_rate': '.sort_menu > li:nth-child(4) > a:nth-child(1)'
    }

    def search(self, query):
        field = self.driver.find_element_by_css_selector(self.selectors['self'])
        field.clear()
        field.send_keys(query)
        field.send_keys(Keys.ENTER)

    @property
    def query(self):
        return self.driver.find_element_by_css_selector(self.selectors['self']).get_attribute('value')

    def sort_by_relevation(self):
        self.driver.find_element_by_css_selector(self.selectors['sort_relevation']).click()

    def sort_by_time(self):
        self.driver.find_element_by_css_selector(self.selectors['sort_time']).click()

    def sort_by_rate(self):
        self.driver.find_element_by_css_selector(self.selectors['sort_rate']).click()