__author__ = 'jk'
# -*- coding: utf-8 -*-
from unittest import TestCase
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


# Тестовый класс
class SeleniumTest(TestCase):
    # Настройка окружения
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://habrahabr.ru/"

    # Тестирует поиск запроса слишком короткой длины
    def test_search_short_string(self):
        driver = self.driver
        driver.get(self.base_url + "search/")
        elem = driver.find_element_by_css_selector("#inner_search_form > input[name=\"q\"]")
        elem.clear()
        elem.send_keys("a")
        elem.send_keys(Keys.ENTER)
        self.assertEqual(u"Сожалеем, поиск в топиках не дал результатов", driver.find_element_by_css_selector("h2.search-results-title").text)

    # Тестирует поиск корректного запроса
    def test_search_true_string(self):
        driver = self.driver
        driver.get(self.base_url + "search/")
        elem = driver.find_element_by_css_selector("#inner_search_form > input[name=\"q\"]")
        elem.clear()
        elem.send_keys("windows 10")
        elem.send_keys(Keys.ENTER)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, u"Как я перестал бояться и полюбил Windows 10"))

    # Проверяет наличие элемента на странице
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    # Освобождение ресурсов
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()