__author__ = 'jk'
# -*- coding: utf-8 -*-


from Components.search_page import SearchPage
from unittest import TestCase
import unittest
from selenium import webdriver

class SeleniumTest(TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.base_url = "http://habrahabr.ru"
        cls.page = SearchPage(cls.driver)
        cls.page.open(cls.base_url + '/search')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Ищет конкретную статью
    def test_search_post(self):
        request = u'Skype. Как мы его любим и одновременно ненавидим. Долгое время, Skype был единственной программой, которую я старался закрывать при работе лаптопа от батареи: потреблял около 4% CPU, будил процессор 250-300 раз в секунду, ничего при этом не делая, оставляя процессору меньше времени на нахождение в более энергосберегающем состоянии.'
        page = self.page
        page.search_bar.search(request)
        self.assertEqual(1, page.search_results.posts, u'Количество постов не равно 1')

    # Ищет конкретный хаб
    def test_search_hub(self):
        request = u'Блог компании «ФогСофт»'
        page = self.page
        page.search_bar.search(request)
        self.assertEqual(1, page.search_results.hubs, u'Количество хабов не равно 1')

    # Ищет конкретного пользователя
    def test_search_user(self):
        request = 'alizar'
        page = self.page
        page.search_bar.search(request)
        self.assertEqual(1, page.search_results.users, u'Количество пользователей не равно 1')

    # Ищет конкретный комментарий
    def test_search_comment(self):
        request = u'Спасибо за заголовок. Неумолимо скатываюсь к шутке про «я построю свой бар с блэкдеком и принцессами». Свежо. получилось. '
        page = self.page
        page.search_bar.search(request)
        self.assertEqual(1, page.search_results.comments, u'Количество комментариев не равно 1')

    # Запрос с отсутствием результатов
    def test_search_none_results(self):
        request = 'zzzzxxxxxxxdddddd'
        page = self.page
        page.search_bar.search(request)
        self.assertEqual(0, page.search_results.sum_res, u'Был найден результат по несуществующему запросу')

    # Популярный запрос
    def test_search_hot_request(self):
        request = 'test'
        page = self.page
        page.search_bar.search(request)
        self.assertLess(1000, page.search_results.sum_res, u'Было найдено слишком мало результатов')

if __name__ == '__main__':
    unittest.main()