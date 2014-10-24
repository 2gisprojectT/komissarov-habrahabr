from online.helpers.base_component import BaseComponent


class SearchResult(BaseComponent):

    selectors = {
        'self': '.searchResults__list',
        'results': '.mixedResults__firmsTabNum'
    }

    @property
    def has_results(self):
        return self.driver.find_element_by_css_selector(self.selectors['results']).is_displayed()
