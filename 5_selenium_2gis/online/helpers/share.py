__author__ = 'jk'
# -*- coding: utf-8 -*-
from online.helpers.base_component import BaseComponent


class SharePanel(BaseComponent):

    selectors = {
        'self': '.extras__share',
        'bar': '#module-1-15',
        'link': '.share__popupUrlInput'
    }

    def share(self):
        self.driver.find_element_by_css_selector(self.selectors['self']).click()

    @property
    def link(self):
        return self.driver.find_element_by_css_selector(self.selectors['link']).get_attribute('value')