__author__ = 'jk'
# -*- coding: utf-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from online.helpers.page import Page


class SeleniumTest(TestCase):
    def test_search(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        request = u'кафе'
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search_by_name(request)
        page.share_panel.share()
        link = page.share_panel.link
        page.open(link)
        self.assertEqual(request, page.search_bar.request)
        driver.close()

    def test_way(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)
        page.open("http://2gis.ru")
        page.search_bar.search_by_way(u'Маркса', u'Студенческая')
        self.assertTrue(page.way_result.is_displayed, 'No results panel')
        driver.close()


if __name__ == '__main__':
    unittest.main()
