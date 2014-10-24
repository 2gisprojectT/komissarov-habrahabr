__author__ = 'jk'
# -*- coding: utf-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from online.helpers.page import Page


class SeleniumTest(TestCase):
    driver = None

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

    def test_search(self):
        request = u'кафе'
        page = self.page
        page.search_bar.search_by_name(request)
        page.share_panel.share()
        link = page.share_panel.link
        page.open(link)
        #self.assertEqual(request, page.search_bar.request)
        self.assertIsNotNone(page.search_bar.request)

    def test_way(self):
        page = self.page
        page.search_bar.search_by_way(u'Маркса', u'Студенческая')
        self.assertTrue(page.way_result.is_displayed, 'No results panel')

if __name__ == '__main__':
    unittest.main()
