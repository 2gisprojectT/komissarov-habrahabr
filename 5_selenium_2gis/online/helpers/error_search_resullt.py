from online.helpers.base_component import BaseComponent


class ErrorSearchResult(BaseComponent):

    selectors = {
        'self': '._error_catalogNotFound',
        'no_results': '.noResults__title'
    }

    @property
    def has_no_results(self):
        return self.driver.find_element_by_css_selector(self.selectors['no_results']).is_displayed()