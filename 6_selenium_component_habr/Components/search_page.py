from search_results import SearchResults
from search_bar import SearchBar


class SearchPage():
    def __init__(self, driver):
        self.driver = driver
        self._search_bar = None
        self._search_results = None

    @property
    def search_bar(self):
        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver,
                                         self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def search_results(self):
        if self._search_results is None:
            self._search_results = SearchResults(self.driver,
                                                 self.driver.find_element_by_css_selector(
                                                     SearchResults.selectors['self']))
        return self._search_results

    def open(self, url):
        self.driver.get(url)