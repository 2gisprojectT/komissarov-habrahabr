__author__ = 'jk'
# -*- coding: utf-8 -*-
from unittest_data_provider import data_provider
from unittest import TestCase
import unittest
from selenium import webdriver
from online.helpers.page import Page


class SeleniumTest(TestCase):
    driver = None

    pos_requests = lambda: (
        (u'кафе',),
        (u'бар',),
        (u'метро',)
    )

    neg_requests = lambda: (
        (u'фффпеанфегеа',),
        (u'1111111111',),
        (u'asdffasf',)
    )

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.base_url = "http://2gis.ru"
        cls.page = Page(cls.driver)
        cls.page.open(cls.base_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data_provider(pos_requests)
    def test_positive_search(self, request):
        page = self.page
        page.search_bar.clear_input()
        page.search_bar.search_by_name(request)
        self.assertTrue(page.search_result.has_results)

    @data_provider(neg_requests)
    def test_negative_search(self, request):
        page = self.page
        page.search_bar.clear_input()
        page.search_bar.search_by_name(request)
        self.assertTrue(page.error_search_result.has_no_results)


if __name__ == '__main__':
    unittest.main()
