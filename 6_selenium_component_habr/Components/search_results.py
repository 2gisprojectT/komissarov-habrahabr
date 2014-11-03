from base_component import BaseComponent
import re

__author__ = 'jk'
# -*- coding: utf-8 -*-


def _parse_(string):
    return int(re.match(r'\d+', string).group())


class SearchResults(BaseComponent):
    selectors = {
        'self': '.menu',
        'posts': 'td.item:nth-child(1) > a:nth-child(1) > span:nth-child(1)',
        'hubs': 'td.item:nth-child(2) > a:nth-child(1) > span:nth-child(1)',
        'users': 'td.item:nth-child(3) > a:nth-child(1) > span:nth-child(1)',
        'comments': 'td.item:nth-child(4) > a:nth-child(1) > span:nth-child(1)'
    }

    @property
    def posts(self):
        return _parse_(self.driver.find_element_by_css_selector(self.selectors['posts']).text)

    @property
    def hubs(self):
        return _parse_(self.driver.find_element_by_css_selector(self.selectors['hubs']).text)

    @property
    def users(self):
        return _parse_(self.driver.find_element_by_css_selector(self.selectors['users']).text)

    @property
    def comments(self):
        return _parse_(self.driver.find_element_by_css_selector(self.selectors['comments']).text)

    @property
    def sum_res(self):
        return self.posts + self.hubs + self.comments + self.users